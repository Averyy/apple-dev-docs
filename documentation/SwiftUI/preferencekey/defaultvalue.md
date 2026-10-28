# defaultValue

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property  
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

## Discussion

Views that have no explicit value for the key produce this default value. Combining child views may remove an implicit value produced by using the default. This means that `reduce(value: &x, nextValue: {defaultValue})` shouldn’t change the meaning of `x`.

## Default Implementations

### PreferenceKey Implementations
- [static var defaultValue: Self.Value](./defaultvalue-23qgw.md)
  Let nil-expressible values default-initialize to nil.

## See Also

### Getting the default value
- [associatedtype Value](./value.md)
  The type of value produced by this preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/preferencekey/defaultvalue)*