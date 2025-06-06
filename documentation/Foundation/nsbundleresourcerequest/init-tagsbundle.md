# init(tags:bundle:)

**Framework**: Foundation  
**Kind**: init

Initializes a resource request for managing the on-demand resources marked with any of the set of specified tags. The managed resources are loaded into the specified bundle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(tags: Set<String>, bundle: Bundle)
```

#### Return Value

The initialized resource request.

## Parameters

- `tags`: A set of strings, with each string specifying a tag assigned to resources stored in  . The value must not be  .
- `bundle`: The bundle used to store the loaded resources. Pass   for the main bundle. The bundle must be the same as the one used in the Xcode project for all the resources marked with the specified tags.

## See Also

- [convenience init(tags: Set<String>)](nsbundleresourcerequest/init(tags:).md)
  Initializes a resource request for managing the on-demand resources marked with any of the set of specified tags. The managed resources are loaded into the main bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/init(tags:bundle:))*