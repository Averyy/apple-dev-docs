# init(format:_:)

**Framework**: ClockKit  
**Kind**: init

Creates and returns a text provider built from the specified format string.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
convenience init(format: String, _ args: any CVarArg...)
```

#### Return Value

A text provider object built from the specified arguments.

#### Discussion

Use this method to create a text provider comprising text and the content of other objects, including other text providers.

## Parameters

- `format`: A format string to use when building the text provider. To insert content from another text provider into the string, use the   placeholder. For more information and examples about the placeholders you can use in this string, see   and  . This parameter must not be  .
- `args`: A comma-separated list of arguments to substitute into  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktextprovider/init(format:_:))*