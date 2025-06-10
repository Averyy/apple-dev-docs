# init(stringInterpolation:)

**Framework**: App Intents  
**Kind**: init

Creates an instance from a string interpolation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(stringInterpolation: IntentURLRepresentation<Intent>.StringInterpolation)
```

#### Discussion

Most `StringInterpolation` types will store information about the literals and interpolations appended to them in one or more properties. `init(stringInterpolation:)` should use these properties to initialize the instance.

## Parameters

- `stringInterpolation`: An instance of    which has had each segment of the string literal appended   to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intenturlrepresentation/init(stringinterpolation:))*