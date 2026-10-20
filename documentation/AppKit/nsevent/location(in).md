# location(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the location of the receiver in the coordinate system of the given node.

**Availability**:
- macOS

## Declaration

```swift
func location(in node: SKNode) -> CGPoint
```

```objc
- (CGPoint) locationInNode:(SKNode *) node;
```

#### Return Value

The location of the event in the node’s coordinate system.

## Parameters

- `node`: A node that is a descendant of a scene presented in the window that received the mouse event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/location(in:))*