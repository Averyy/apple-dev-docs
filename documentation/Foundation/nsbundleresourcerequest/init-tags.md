# init(tags:)

**Framework**: Foundation  
**Kind**: init

Initializes a resource request for managing the on-demand resources marked with any of the set of specified tags. The managed resources are loaded into the main bundle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(tags: Set<String>)
```

#### Return Value

The initialized resource request.

## Parameters

- `tags`: A set of strings, with each string specifying a tag assigned to resources stored in the main bundle. The value must not be  .

## See Also

- [class Bundle](bundle.md)
  A representation of the code and resources stored in a bundle directory on disk.
- [On-Demand Resources Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/index.html#//apple_ref/doc/uid/TP40015083)
- [init(tags: Set<String>, bundle: Bundle)](nsbundleresourcerequest/init(tags:bundle:).md)
  Initializes a resource request for managing the on-demand resources marked with any of the set of specified tags. The managed resources are loaded into the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/init(tags:))*