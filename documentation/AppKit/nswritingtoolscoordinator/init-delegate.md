# init(delegate:)

**Framework**: AppKit  
**Kind**: init

Creates a writing tools coordinator and assigns the specified delegate object to it.

**Availability**:
- macOS 15.2+

## Declaration

```swift
@MainActor
init(delegate: (any NSWritingToolsCoordinator.Delegate)?)
```

#### Discussion

Create the coordinator object during your view’s initialization, and assign the object to your view. Assign the coordinator to the [`writingToolsCoordinator`](nsview/writingtoolscoordinator.md) property of your view.

## Parameters

- `delegate`: An object capable of handling Writing Tools interactions   for your view. The delegate must be able to modify your view’s text   storage and refresh the view’s layout and appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/init(delegate:))*