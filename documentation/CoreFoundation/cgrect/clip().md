# clip()

**Framework**: Core Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the current graphics context clipping path by intersecting it with this rect. This permanently modifies the graphics state, so the current state should be saved beforehand and restored afterwards.

**Availability**:
- macOS 10.9+
- Swift 4.0+

## Declaration

```swift
func clip()
```

#### Discussion

> **Precondition**: There must be a set current NSGraphicsContext.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cgrect/clip())*