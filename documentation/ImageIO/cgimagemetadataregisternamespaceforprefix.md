# CGImageMetadataRegisterNamespaceForPrefix(_:_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Registers the specified namespace and prefix with the metadata object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGImageMetadataRegisterNamespaceForPrefix(_ metadata: CGMutableImageMetadata, _ xmlns: CFString, _ prefix: CFString, _ err: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool
```

#### Return Value

`true` if registration of the namespace was successful, or `false` if it wasn’t.

#### Discussion

All tags you add to a [`CGMutableImageMetadata`](cgmutableimagemetadata.md) object must belong to known namespaces. When you encounter an unrecognized prefix in a metadata path, call this function to register the prefix before you add the corresponding tag.

You don’t need to register the standard metadata spaces, or any metadata spaces that are already present in the image’s metadata. Register only the namespaces you need to support additional metadata tags.

If the namespace already exists and the `prefix` parameter conflicts with the already registered prefix, this function returns `false` and places an error object in the `err` parameter. However, if the prefix matches what’s registered, this method returns `true`.

## Parameters

- `metadata`: The metadata object in which to register the namespace.
- `xmlns`: The namespace to register. Specify a string with a custom namespace URI. A custom namespace must be a valid XML namespace. By convention, namespaces end with either the   or   character.
- `prefix`: An abbreviation for the XML namespace. You must specify a valid string for custom namespace.
- `err`: A pointer to an error object. If an error occurs, this function assigns an error object to this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadataregisternamespaceforprefix(_:_:_:_:))*