# displayPadding

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

Returns the size of the extra padding added to any drawing layer used to rasterize the text. For example when drawing the text with a shadow this may be used to extend the drawing bounds to avoid clipping the shadow.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var displayPadding: EdgeInsets { get }
```

#### Discussion

The default implementation of this function returns an empty set of insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textrenderer/displaypadding)*