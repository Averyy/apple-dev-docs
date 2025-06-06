# description

**Framework**: SwiftUI  
**Kind**: property

A textual representation of the color.

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
var description: String { get }
```

#### Discussion

Use this method to get a string that represents the color. The [`print(_:separator:terminator:)`](https://developer.apple.com/documentation/Swift/print(_:separator:terminator:)) function uses this property to get a string representing an instance:

```swift
print(Color.red)
// Prints "red"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/description)*