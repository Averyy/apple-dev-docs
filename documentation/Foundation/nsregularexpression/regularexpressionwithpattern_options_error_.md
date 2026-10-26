# regularExpressionWithPattern:options:error:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates an NSRegularExpression instance with the specified regular expression pattern and options.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (NSRegularExpression *) regularExpressionWithPattern:(NSString *) pattern options:(NSRegularExpressionOptions) options error:(NSError **) error;
```

#### Return Value

An instance of `NSRegularExpression` for the specified regular expression and options.

## Parameters

- `pattern`: The regular expression pattern to compile.
- `options`: The matching options. See [`NSRegularExpression.Options`](./options-swift.struct.md) for possible values. The values can be combined using the C-bitwise `OR` operator.
- `error`: An out value that returns any error encountered during initialization. Returns an `NSError` object if the regular expression pattern is invalid; otherwise returns `nil`.

## See Also

### Creating Regular Expressions
- [init(pattern: String, options: NSRegularExpression.Options) throws](./init%28pattern,options%29.md)
  Returns an initialized NSRegularExpression instance with the specified regular expression pattern and options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/regularexpressionwithpattern:options:error:)*