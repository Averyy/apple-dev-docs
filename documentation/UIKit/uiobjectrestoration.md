# UIObjectRestoration

**Framework**: UIKit  
**Kind**: protocol

The interface that restoration classes use to restore preserved objects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIObjectRestoration
```

#### Overview

A restorable object must set its [`objectRestorationClass`](uistaterestoring/objectrestorationclass.md) property to the class that adopts this protocol. The method in this protocol should be used to return the object if it already exists or create it if needed.

## Topics

### Creating the restorable object
- [static func object(withRestorationIdentifierPath: [String], coder: NSCoder) -> (any UIStateRestoring)?](uiobjectrestoration/object(withrestorationidentifierpath:coder:).md)
  Requests the object that corresponds to the specified identifier information.

## See Also

- [Restoring your app’s state](restoring-your-app-s-state.md)
  Provide continuity for the user by preserving current activities.
- [Restoring your app’s state with SwiftUI](../SwiftUI/restoring-your-app-s-state-with-swiftui.md)
  Provide app continuity for users by preserving their current activities.
- [Preserving your app’s UI across launches](preserving-your-app-s-ui-across-launches.md)
  Return your app to its previous state after the system terminates it.
- [protocol UIViewControllerRestoration](uiviewcontrollerrestoration.md)
  The methods that objects adopt so that they can act as a restoration class for view controllers during state restoration.
- [protocol UIStateRestoring](uistaterestoring.md)
  Methods for adding objects to your state restoration archives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiobjectrestoration)*