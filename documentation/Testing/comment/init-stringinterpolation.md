# init(stringInterpolation:)

**Framework**: Swift Testing  
**Kind**: init

Creates an instance from a string interpolation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
init(stringInterpolation: Comment.StringInterpolation)
```

#### Discussion

Most `StringInterpolation` types will store information about the literals and interpolations appended to them in one or more properties. `init(stringInterpolation:)` should use these properties to initialize the instance.

## Parameters

- `stringInterpolation`: An instance of    which has had each segment of the string literal appended   to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/comment/init(stringinterpolation:))*