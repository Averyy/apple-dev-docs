# defaultValue

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

The default value of the preference.

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
static var defaultValue: Self.Value { get }
```

#### Discussion

Views that have no explicit value for the key produce this default value. Combining child views may remove an implicit value produced by using the default. This means that `reduce(value: &x, nextValue: {defaultValue})` shouldn’t change the meaning of `x`.

## See Also

- [associatedtype Value](preferencekey/value.md)
  The type of value produced by this preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/preferencekey/defaultvalue)*