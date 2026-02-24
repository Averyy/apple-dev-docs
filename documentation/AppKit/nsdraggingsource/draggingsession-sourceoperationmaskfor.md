# draggingSession(_:sourceOperationMaskFor:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Declares the types of operations the source allows to be performed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func draggingSession(_ session: NSDraggingSession, sourceOperationMaskFor context: NSDraggingContext) -> NSDragOperation
```

#### Return Value

A dragging operation you specify.

#### Discussion

To account for unexpected contexts, set a `default` case for the most specific context your app handles. The following code shows an example that handles different dragging contexts and includes a default case.

```objc
    switch(context) {
        case NSDraggingContextOutsideApplication:
            return NSDragOperationCopy;
 
        case NSDraggingContextWithinApplication:
        default:
            return NSDragOperationCopy | NSDragOperationMove;
    }
```

## Parameters

- `session`: The dragging session.
- `context`: The dragging context. See [`NSDraggingContext`](nsdraggingcontext.md) for the supported values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsource/draggingsession(_:sourceoperationmaskfor:))*