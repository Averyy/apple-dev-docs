# init(pattern:options:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an initialized NSRegularExpression instance with the specified regular expression pattern and options.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(pattern: String, options: NSRegularExpression.Options = []) throws
```

```objc
- (instancetype) initWithPattern:(NSString *) pattern options:(NSRegularExpressionOptions) options error:(NSError **) error;
```

## Return Value

An instance of `NSRegularExpression` for the specified regular expression and options.

## Discussion

> **Handling Errors in Swift**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `pattern`: The regular expression pattern to compile.
- `options`: The regular expression options that are applied to the expression during matching. See [`NSRegularExpression.Options`](./options-swift.struct.md) for possible values.

## See Also

### Related Documentation
- [+ regularExpressionWithPattern:options:error:](./regularexpressionwithpattern_options_error_.md)
  Creates an NSRegularExpression instance with the specified regular expression pattern and options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/init(pattern:options:))*