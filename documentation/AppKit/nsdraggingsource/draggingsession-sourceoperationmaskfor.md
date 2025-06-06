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

The appropriate dragging operation as defined in

#### Discussion

In the future Apple may provide more specific “within” values in the future. To account for this, for unrecognized localities, return the operation mask for the most specific context that you are concerned with. The following code is an example of how to implement this functionality:

```objc
    switch(context) {
        case NSDraggingContextOutsideApplication:
            return ...
            break;
 
        case NSDraggingContextWithinApplication:
        default:
            return ...
            break;
    }
```

## Parameters

- `session`: The dragging session.
- `context`: The dragging context. See   for the supported values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsource/draggingsession(_:sourceoperationmaskfor:))*