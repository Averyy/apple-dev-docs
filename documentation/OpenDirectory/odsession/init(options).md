# init(options:)

**Framework**: Open Directory  
**Kind**: init  
**Role**: Initializer

Creates a session object directed over proxy to another host.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
init(options inOptions: [AnyHashable : Any]! = [:]) throws
```

```objc
- (instancetype) initWithOptions:(NSDictionary *) inOptions error:(NSError **) outError;
```

#### Return Value

The created session object.

#### Discussion

> **Handling Errors in Swift**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inOptions`: A dictionary of options to associate with the session. Can be `nil`.

## See Also

### Related Documentation
- [class ODSession](../odsession.md)
  An `ODSession` object serves as a Cocoa wrapper for an Open Directory session.
### Creating and Accessing Sessions
- [class func `default`() -> ODSession!](./default%28%29.md)
  Returns a shared instance of the local session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odsession/init(options:))*