# init(stringInterpolation:)

**Framework**: App Intents  
**Kind**: init

Creates an instance from a string interpolation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
init(stringInterpolation: AppShortcutParameterPresentationTitleString<Intent, Value, Parameter, ParameterKeyPath>.StringInterpolation)
```

#### Discussion

Most `StringInterpolation` types will store information about the literals and interpolations appended to them in one or more properties. `init(stringInterpolation:)` should use these properties to initialize the instance.

## Parameters

- `stringInterpolation`: An instance of    which has had each segment of the string literal appended   to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutparameterpresentationtitlestring/init(stringinterpolation:))*