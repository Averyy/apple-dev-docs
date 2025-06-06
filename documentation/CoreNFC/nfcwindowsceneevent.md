# NFCWindowSceneEvent

**Framework**: Core NFC  
**Kind**: enum

An NFC-related event that your app uses to update its user interface.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+

## Declaration

```swift
enum NFCWindowSceneEvent
```

#### Overview

When the device is eligible to receive NFC-related events, this type indicates the type of received event. The event may indicate the presence of an NFC reader or a gesture by the person using the app to initiate a contactless transaction. [`NFCWindowSceneEvent`](nfcwindowsceneevent.md) represents these as the [`NFCWindowSceneEvent.readerDetected`](nfcwindowsceneevent/readerdetected.md) and [`NFCWindowSceneEvent.presentation`](nfcwindowsceneevent/presentation.md) cases, respectively.

You can receive this event in two scenarios:

- When the system calls [`UISceneDelegate`](https://developer.apple.com/documentation/UIKit/UISceneDelegate) method [`scene(_:willConnectTo:options:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/scene(_:willConnectTo:options:)), the system created a new scene in response to the event. In this case, check the `connectionOptions` parameter for the presence of the [`nfcEvent`](https://developer.apple.com/documentation/UIKit/UIScene/ConnectionOptions/nfcEvent) member, which is an instance of [`NFCWindowSceneEvent`](nfcwindowsceneevent.md).
- When the system calls the [`NFCWindowSceneDelegate`](nfcwindowscenedelegate.md) method [`windowScene(_:didReceiveNFCWindowSceneEvent:)`](nfcwindowscenedelegate/windowscene(_:didreceivenfcwindowsceneevent:).md), the system delivered the event to an existing scene.

In either case, store the event and use it to update the UI for an NFC interaction. The following example shows a scene delegate that handles both scenarios, using a `ViewModel` class to store the event for use by an appropriate view:

```swift
import UIKit
import SwiftUI
import CoreNFC

class SceneDelegate: UIResponder, UIWindowSceneDelegate, NFCWindowSceneDelegate {

    var window: UIWindow?
    var myViewModel = ViewModel()

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        guard let windowScene = (scene as? UIWindowScene) else { return }
        
        // Check the connection options to see if the scene is being created
        // in response to an NFC event.
        guard let nfcEvent = connectionOptions.nfcEvent  else { return }
        // If there's an event, update the view model.
        myViewModel.receivedNFCEvent = nfcEvent

        // Update the view hierarchy by using myViewModel to create a new
        // view.
    }

    func windowScene(_ windowScene: UIWindowScene, didReceiveNFCWindowSceneEvent event: NFCWindowSceneEvent) {
        // Update the view model with the NFC event.
        myViewModel.receivedNFCEvent = event
        // Update the view hierarchy by using myViewModel to create a new
        // view.
     }
}
```

## Topics

### Events
- [NFCWindowSceneEvent.readerDetected](nfcwindowsceneevent/readerdetected.md)
  The eligible device detected the RF field of an NFC reader.
- [NFCWindowSceneEvent.presentation](nfcwindowsceneevent/presentation.md)
  The user performed a gesture to present an NFC display.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [protocol NFCWindowSceneDelegate](nfcwindowscenedelegate.md)
  A protocol to notify your app’s user interface about NFC-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcwindowsceneevent)*