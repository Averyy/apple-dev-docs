# init(literalCapacity:interpolationCount:)

**Framework**: App Intents  
**Kind**: init

Creates an empty instance ready to be filled with string literal content.

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
init(literalCapacity: Int, interpolationCount: Int)
```

#### Discussion

Don’t call this initializer directly. Instead, initialize a variable or constant using a string literal with interpolated expressions.

Swift passes this initializer a pair of arguments specifying the size of the literal segments and the number of interpolated segments. Use this information to estimate the amount of storage you will need.

## Parameters

- `literalCapacity`: The approximate size of all literal segments   combined. This is meant to be passed to  ;   it may be slightly larger or smaller than the sum of the counts of each   literal segment.
- `interpolationCount`: The number of interpolations which will be   appended. Use this value to estimate how much additional capacity will   be needed for the interpolated segments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intenturlrepresentation/stringinterpolation/init(literalcapacity:interpolationcount:))*