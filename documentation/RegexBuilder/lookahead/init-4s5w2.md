# init(_:)

**Framework**: RegexBuilder  
**Kind**: init

Creates a lookahead from the given regex component.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init<R>(_ component: R) where Output == R.RegexOutput, R : RegexComponent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/lookahead/init(_:)-4s5w2)*