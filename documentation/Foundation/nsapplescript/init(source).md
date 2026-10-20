# init(source:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated script instance from the passed source.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init?(source: String)
```

```objc
- (instancetype) initWithSource:(NSString *) source;
```

#### Return Value

The initialized script object, `nil` if an error occurs.

#### Discussion

This method is a designated initializer for `NSAppleScript`.

## Parameters

- `source`: A string containing the source code of a script.

## See Also

### Initializing a Script
- [init?(contentsOf: URL, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./init%28contentsof,error%29.md)
  Initializes a newly allocated script instance from the source identified by the passed URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsapplescript/init(source:))*