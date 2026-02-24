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

- `format`: A format string to use when building the text provider. To insert content from another text provider into the string, use the `%@` placeholder. For more information and examples about the placeholders you can use in this string, see [`Formatting String Objects`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943) and [`String Format Specifiers`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265). This parameter must not be `nil`.
- `args`: A comma-separated list of arguments to substitute into `format`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktextprovider/init(format:_:))*