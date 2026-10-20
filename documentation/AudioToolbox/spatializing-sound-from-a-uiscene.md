# Anchoring sound to a window or volume

**Framework**: Audio Toolbox  
**Role**: Article

Provide unique app experiences by attaching sounds to windows and volumes in 3D space.

#### Overview

Many audio playback APIs have a property to configure their 3D spatial rendering using the [`SpatialAudioExperience`](./spatialaudioexperience.md) type [`HeadTrackedSpatialAudio`](./headtrackedspatialaudio.md). This article shows how to take advantage of [`HeadTrackedSpatialAudio`](./headtrackedspatialaudio.md) to place each sound at the center of its intended [`UIScene`](../UIKit/uiscene.md) in your multiwindow or multivolume application.

![An illustration of sound spatializing from two windows.](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spatializing-sound-from-a-uiscene-01@2x.png)

#### Get the scene’s identifier

Placing a sound on a specific [`UIScene`](../UIKit/uiscene.md) requires knowledge of the target scene’s [`persistentIdentifier`](../UIKit/uiscenesession/persistentidentifier.md). In a SwiftUI application, that means adding both a [`UIApplicationDelegate`](../UIKit/uiapplicationdelegate.md) and [`UISceneDelegate`](../UIKit/uiscenedelegate.md) to your SwiftUI App:

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

The following code makes the identifier for each [`UIScene`](../UIKit/uiscene.md) accessible from any SwiftUI [`View`](../SwiftUI/view.md) using your [`UISceneDelegate`](../UIKit/uiscenedelegate.md) as an [`EnvironmentObject`](../SwiftUI/environmentobject.md):

```swift
import SwiftUI

struct ContentView: View {
    @EnvironmentObject var sceneDelegate: MySceneDelegate

    var body: some View {
        Text("\(String(describing: sceneDelegate.sceneIdentifier))")
    }
}
```

#### Anchor the sound to the scene

With a [`UIScene`](../UIKit/uiscene.md) identifier in-hand, configure each sound using a [`HeadTrackedSpatialAudio`](./headtrackedspatialaudio.md) structure.

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

Besides just [`AVAudioPlayer`](../AVFAudio/avaudioplayer.md), you can also use [`SpatialAudioExperience`](./spatialaudioexperience.md) types with the other playback APIs listed below.

#### Spatialize system and alert sounds

Configure the spatial audio experience of your system and alert sounds using:

- [`AudioServicesPlaySystemSound(_:spatialExperience:)`](./audioservicesplaysystemsound%28_,spatialexperience%29.md)
- [`AudioServicesPlayAlertSound(_:spatialExperience:)`](./audioservicesplayalertsound%28_,spatialexperience%29.md)

#### Spatialize audio-only playback APIs

Configure the spatial audio experience of audio-only playback APIs using the [`intendedSpatialExperience`](../AVFAudio/avaudioplayer/intendedspatialexperience-27klj.md) property on:

- [AVAudioPlayer](../AVFAudio/avaudioplayer/intendedspatialexperience-27klj.md)
- [AVAudioOutputNode](../AVFAudio/avaudiooutputnode/intendedspatialexperience-3ts59.md)
- [AUAudioUnit](./auaudiounit/intendedspatialexperience-7uqrm.md)
- [CHHapticEngine](../CoreHaptics/chhapticengine/intendedspatialexperience-55ca0.md)

#### Spatialize audio playback APIs that also have video

Setting a scene identifier on playback APIs that have video content isn’t always necessary as their sound automatically anchors to its visual counterpart. However, if there is no video or if you prefer something besides the automatic behavior, configure the spatial audio experience of these playback APIs using the [`intendedSpatialAudioExperience`](../AVFoundation/avplayer/intendedspatialaudioexperience-1bd87.md) property on:

- [AVPlayer](../AVFoundation/avplayer/intendedspatialaudioexperience-1bd87.md)
- [AVSampleBufferRenderSynchronizer](../AVFoundation/avsamplebufferrendersynchronizer/intendedspatialaudioexperience-3z7d3.md)

## See Also

### Playback and Recording
- [Audio Queue Services](./audio-queue-services.md)
  Connect to audio hardware and manage the recording or playback process.
- [Audio Services](./audio-services.md)
  Play short sounds or trigger a vibration effect on iOS devices with the appropriate hardware.
- [Music Player](./music-player.md)
  Create and play a sequence of tracks, and manage aspects of playback in response to standard events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/spatializing-sound-from-a-uiscene)*