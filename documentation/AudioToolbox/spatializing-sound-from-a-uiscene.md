# Anchoring sound to a window or volume

**Framework**: Audio Toolbox

Provide unique app experiences by attaching sounds to windows and volumes in 3D space.

#### Overview

Many audio playback APIs have a property to configure their 3D spatial rendering using the [`SpatialAudioExperience`](spatialaudioexperience.md) type [`HeadTrackedSpatialAudio`](headtrackedspatialaudio.md). This article shows how to take advantage of [`HeadTrackedSpatialAudio`](headtrackedspatialaudio.md) to place each sound at the center of its intended [`UIScene`](https://developer.apple.com/documentation/UIKit/UIScene) in your multiwindow or multivolume application.

![An illustration of sound spatializing from two windows.](https://docs-assets.developer.apple.com/published/323964a84b824963178ea5b99ae51260/spatializing-sound-from-a-uiscene-01%402x.png)

#### Get the Scenes Identifier

Placing a sound on a specific [`UIScene`](https://developer.apple.com/documentation/UIKit/UIScene) requires knowledge of the target scene’s [`persistentIdentifier`](https://developer.apple.com/documentation/UIKit/UISceneSession/persistentIdentifier). In a SwiftUI application, that means adding both a [`UIApplicationDelegate`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate) and [`UISceneDelegate`](https://developer.apple.com/documentation/UIKit/UISceneDelegate) to your SwiftUI App:

```swift
import SwiftUI 

@main
struct MyApplication: App {
    @UIApplicationDelegateAdaptor var delegate: MyAppDelegate

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

class MyAppDelegate: NSObject, UIApplicationDelegate, ObservableObject {
    func application(_ application: UIApplication,
                     configurationForConnecting connectingSceneSession: UISceneSession,
                     options: UIScene.ConnectionOptions) -> UISceneConfiguration {
        let sceneConfig = UISceneConfiguration(name: nil, sessionRole: connectingSceneSession.role)
        sceneConfig.delegateClass = MySceneDelegate.self
        return sceneConfig
    }
}

class MySceneDelegate: NSObject, UISceneDelegate, ObservableObject {
    var sceneIdentifier: String?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        sceneIdentifier = session.persistentIdentifier
    }
}
```

The following code makes the identifier for each [`UIScene`](https://developer.apple.com/documentation/UIKit/UIScene) accessible from any SwiftUI [`View`](https://developer.apple.com/documentation/SwiftUI/View) using your [`UISceneDelegate`](https://developer.apple.com/documentation/UIKit/UISceneDelegate) as an [`EnvironmentObject`](https://developer.apple.com/documentation/SwiftUI/EnvironmentObject):

```swift
import SwiftUI

struct ContentView: View {
    @EnvironmentObject var sceneDelegate: MySceneDelegate

    var body: some View {
        Text("\(String(describing: sceneDelegate.sceneIdentifier))")
    }
}
```

#### Anchor the Sound to the Scene

With a [`UIScene`](https://developer.apple.com/documentation/UIKit/UIScene) identifier in-hand, configure each sound using a [`HeadTrackedSpatialAudio`](headtrackedspatialaudio.md) structure.

```swift
import SwiftUI
import AVFAudio

struct ContentView: View {
    @EnvironmentObject var sceneDelegate: MySceneDelegate
    
    @State var player: AVAudioPlayer? = {
        guard let url = Bundle.main.url(forResource: "my_sound", withExtension: "wav") else {
            return nil
        }
        return try? AVAudioPlayer(contentsOf: url)
    }()

    var body: some View {
        Text("Hello, Sound!")
    }
    .onAppear {
        guard let player = self.player, let sceneID = self.sceneDelegate.sceneIdentifier else {
            return
        }
        
        player.intendedSpatialExperience = .headTracked(.scene(identifier: sceneID))
        player.play()
    }
}
```

Besides just [`AVAudioPlayer`](https://developer.apple.com/documentation/AVFAudio/AVAudioPlayer), you can also use [`SpatialAudioExperience`](spatialaudioexperience.md) types with the other playback APIs listed below.

#### Spatialize System and Alert Sounds

Configure the spatial audio experience of your system and alert sounds using:

- [`AudioServicesPlaySystemSound(_:spatialExperience:)`](audioservicesplaysystemsound(_:spatialexperience:).md)
- [`AudioServicesPlayAlertSound(_:spatialExperience:)`](audioservicesplayalertsound(_:spatialexperience:).md)

#### Spatialize Audio Only Playback Apis

Configure the spatial audio experience of audio-only playback APIs using the [`intendedSpatialExperience`](https://developer.apple.com/documentation/AVFAudio/AVAudioPlayer/intendedSpatialExperience-27klj) property on:

- [`intendedSpatialExperience`](https://developer.apple.com/documentation/AVFAudio/AVAudioPlayer/intendedSpatialExperience-27klj)
- [`intendedSpatialExperience`](https://developer.apple.com/documentation/AVFAudio/AVAudioOutputNode/intendedSpatialExperience-3ts59)
- [`intendedSpatialExperience`](AUAudioUnit/intendedSpatialExperience-7uqrm.md)
- [`intendedSpatialExperience`](https://developer.apple.com/documentation/CoreHaptics/CHHapticEngine/intendedSpatialExperience-55ca0)

#### Spatialize Audio Playback Apis That Also Have Video

Setting a scene identifier on playback APIs that have video content isn’t always necessary as their sound automatically anchors to its visual counterpart. However, if there is no video or if you prefer something besides the automatic behavior, configure the spatial audio experience of these playback APIs using the [`intendedSpatialAudioExperience`](https://developer.apple.com/documentation/AVFoundation/AVPlayer/intendedSpatialAudioExperience-1bd87) property on:

- [`intendedSpatialAudioExperience`](https://developer.apple.com/documentation/AVFoundation/AVPlayer/intendedSpatialAudioExperience-1bd87)
- [`intendedSpatialAudioExperience`](https://developer.apple.com/documentation/AVFoundation/AVSampleBufferRenderSynchronizer/intendedSpatialAudioExperience-3z7d3)

## See Also

- [Audio Queue Services](audio-queue-services.md)
  Connect to audio hardware and manage the recording or playback process.
- [Audio Services](audio-services.md)
  Play short sounds or trigger a vibration effect on iOS devices with the appropriate hardware.
- [Music Player](music-player.md)
  Create and play a sequence of tracks, and manage aspects of playback in response to standard events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/spatializing-sound-from-a-uiscene)*