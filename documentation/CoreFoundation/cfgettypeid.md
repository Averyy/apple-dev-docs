# CFGetTypeID(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the unique identifier of an opaque type to which a Core Foundation object belongs.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFGetTypeID(_ cf: CFTypeRef!) -> CFTypeID
```

#### Return Value

A value of type [`CFTypeID`](cftypeid.md) that identifies the opaque type of `cf`.

#### Discussion

This function returns a value that uniquely identifies the opaque type of any Core Foundation object. You can compare this value with the known [`CFTypeID`](cftypeid.md) identifier obtained with a “GetTypeID” function specific to a type, for example [`CFDateGetTypeID()`](cfdategettypeid().md). These values might change from release to release or platform to platform.

## Parameters

- `cf`: The CFType object to examine.

## See Also

- [func CFCopyDescription(CFTypeRef!) -> CFString!](cfcopydescription(_:).md)
  Returns a textual description of a Core Foundation object.
- [func CFCopyTypeIDDescription(CFTypeID) -> CFString!](cfcopytypeiddescription(_:).md)
  Returns a textual description of a Core Foundation type, as identified by its type ID, which can be used when debugging.
- [func CFShow(CFTypeRef!)](cfshow(_:).md)
  Prints a description of a Core Foundation object to stderr.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfgettypeid(_:))*