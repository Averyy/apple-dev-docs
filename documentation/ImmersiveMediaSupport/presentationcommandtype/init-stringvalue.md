# init(stringValue:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a new instance from the given string.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init?(stringValue: String)
```

#### Discussion

If the string passed as `stringValue` does not correspond to any instance of this type, the result is `nil`.

## Parameters

- `stringValue`: The string value of the desired key.

## See Also

- [init?(intValue: Int)](presentationcommandtype/init(intvalue:).md)
  Creates a new instance from the specified integer.
- [init?(rawValue: String)](presentationcommandtype/init(rawvalue:).md)
  Creates a new instance with the specified raw value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationcommandtype/init(stringvalue:))*