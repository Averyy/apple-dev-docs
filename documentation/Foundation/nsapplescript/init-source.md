# init(source:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated script instance from the passed source.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init?(source: String)
```

#### Return Value

The initialized script object, `nil` if an error occurs.

#### Discussion

This method is a designated initializer for `NSAppleScript`.

## Parameters

- `source`: A string containing the source code of a script.

## See Also

- [init?(contentsOf: URL, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsapplescript/init(contentsof:error:).md)
  Initializes a newly allocated script instance from the source identified by the passed URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsapplescript/init(source:))*