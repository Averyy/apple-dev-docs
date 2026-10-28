# current

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Returns the `NSAssertionHandler` object associated with the current thread.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var current: NSAssertionHandler { get }
```

```objc
@property (class, strong, readonly) NSAssertionHandler * currentHandler;
```

## Return Value

The `NSAssertionHandler` object associated with the current thread.

## Discussion

If no assertion handler is associated with the current thread, this method creates one and assigns it to the thread.

## See Also

### Handling Assertion Failures
- [- handleFailureInFunction:file:lineNumber:description:](./handlefailureinfunction_file_linenumber_description_.md)
- [- handleFailureInMethod:object:file:lineNumber:description:](./handlefailureinmethod_object_file_linenumber_description_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsassertionhandler/current)*