# lineLimit

**Framework**: SwiftUI  
**Kind**: property

The maximum number of lines that text can occupy in a view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var lineLimit: Int? { get set }
```

#### Discussion

The maximum number of lines is `1` if the value is less than `1`. If the value is `nil`, the text uses as many lines as required. The default is `nil`.

## See Also

- [func lineLimit(_:)](view/linelimit(_:).md)
  Sets to a closed range the number of lines that text can occupy in this view.
- [func lineLimit(Int, reservesSpace: Bool) -> some View](view/linelimit(_:reservesspace:).md)
  Sets a limit for the number of lines text can occupy in this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/linelimit)*