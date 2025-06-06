# init(stringInterpolation:)

**Framework**: Swift  
**Kind**: init  
**Required**: Yes

Creates an instance from a string interpolation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(stringInterpolation: Self.StringInterpolation)
```

#### Discussion

Most `StringInterpolation` types will store information about the literals and interpolations appended to them in one or more properties. `init(stringInterpolation:)` should use these properties to initialize the instance.

## Parameters

- `stringInterpolation`: An instance of    which has had each segment of the string literal appended   to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/expressiblebystringinterpolation/init(stringinterpolation:))*