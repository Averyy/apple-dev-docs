# LinkMetadata

**Framework**: Link Presentation  
**Kind**: struct

A structure containing metadata about a URL.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)
- watchOS 26.4+ (Beta)

## Declaration

```swift
nonisolated
struct LinkMetadata
```

#### Overview

Use [`LinkMetadata`](linkmetadata.md) to store metadata about a URL, including its title, icon, images, and video.

Fetch metadata using [`LPMetadataProvider`](lpmetadataprovider.md). For remote URLs, cache the metadata locally to avoid the data and performance cost of fetching it from the internet every time you present it. [`LinkMetadata`](linkmetadata.md) is also serializable and conforms to `Codable`.

## Topics

### Structures
- [LinkMetadata.Attachment](linkmetadata/attachment.md)
### Initializers
- [init?(sending LPLinkMetadata)](linkmetadata/init(_:).md)
  Creates a [`LinkMetadata`](linkmetadata.md) value from a [`LPLinkMetadata`](lplinkmetadata.md) instance.
- [init(fetching: URL, timeout: Duration, includeSubresources: Bool) async throws](linkmetadata/init(fetching:timeout:includesubresources:)-69bj2.md)
  Creates a [`LinkMetadata`](linkmetadata.md) value from the specified properties by fetching the specified URL.
- [init(fetching: URLRequest, timeout: Duration, includeSubresources: Bool) async throws](linkmetadata/init(fetching:timeout:includesubresources:)-7rkd9.md)
  Creates a [`LinkMetadata`](linkmetadata.md) value from the specified properties by fetching the URL using the specified request.
- [init<A, B, C>(originalURL: URL?, title: String?, image: A?, icon: B?, video: C?)](linkmetadata/init(originalurl:title:image:icon:video:).md)
- [init(url: URL)](linkmetadata/init(url:).md)
  Creates a new [`LinkMetadata`](linkmetadata.md) value for the specified URL.
### Instance Properties
- [var originalURL: URL](linkmetadata/originalurl.md)
  The original URL of the metadata request.
- [var remoteVideo: URL?](linkmetadata/remotevideo.md)
  A remote URL corresponding to a representative video for the URL
- [var title: String?](linkmetadata/title.md)
  A representative title for the URL.
- [var url: URL](linkmetadata/url.md)
  The URL that returned the metadata, taking server-side redirects into account.
### Instance Methods
- [func containsMedia(LinkMetadata.Attachment, exportableAs: (some Transferable).Type) -> Bool](linkmetadata/containsmedia(_:exportableas:).md)
  Determines if a specific `Transferable` type can be loaded for an attachment in the metadata.
- [func media<Media>(LinkMetadata.Attachment, as: Media.Type) async throws -> Media?](linkmetadata/media(_:as:).md)
  Loads the media data of this metadata for an attachment as the specified Transferable type if possible.
- [func setMedia(some Transferable, for: LinkMetadata.Attachment)](linkmetadata/setmedia(_:for:).md)
  Sets the media data in the metadata for an attachment.
### Type Aliases
- [LinkMetadata.Specification](linkmetadata/specification.md)
- [LinkMetadata.UnwrappedType](linkmetadata/unwrappedtype.md)
- [LinkMetadata.ValueType](linkmetadata/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](linkmetadata/defaultresolverspecification.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [DisplayRepresentable](../AppIntents/DisplayRepresentable.md)
- [Encodable](../Swift/Encodable.md)
- [Escapable](../Swift/Escapable.md)
- [InstanceDisplayRepresentable](../AppIntents/InstanceDisplayRepresentable.md)
- [PersistentlyIdentifiable](../AppIntents/PersistentlyIdentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Transferable](../CoreTransferable/Transferable.md)
- [TypeDisplayRepresentable](../AppIntents/TypeDisplayRepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/linkmetadata)*