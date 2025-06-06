# CGImageDestinationCopyTypeIdentifiers()

**Framework**: Image I/O  
**Kind**: func

Returns an array of the uniform type identifiers that are supported for image destinations.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGImageDestinationCopyTypeIdentifiers() -> CFArray
```

#### Return Value

Returns an array of the uniform type identifiers that image destinations support. For a list of system-declared and third-party identifiers, see [`Uniform Type Identifiers`](https://developer.apple.com/documentation/UniformTypeIdentifiers).

## See Also

- [func CGImageDestinationGetTypeID() -> CFTypeID](cgimagedestinationgettypeid().md)
  Returns the unique type identifier of an image destination opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagedestinationcopytypeidentifiers())*