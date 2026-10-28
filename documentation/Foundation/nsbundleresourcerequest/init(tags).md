# init(tags:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a resource request for managing the on-demand resources marked with any of the set of specified tags. The managed resources are loaded into the main bundle.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

> **Deprecated**: Use Background Assets instead.

## Declaration

```swift
convenience init(tags: Set<String>)
```

```objc
- (instancetype) initWithTags:(NSSet<NSString *> *) tags;
```

## Return Value

The initialized resource request.

## Parameters

- `tags`: A set of strings, with each string specifying a tag assigned to resources stored in the main bundle. The value must not be `nil`.

## See Also

### Related Documentation
- [class Bundle](../bundle.md)
  A representation of the code and resources stored in a bundle directory on disk.
- [On-Demand Resources Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/index.html#//apple_ref/doc/uid/TP40015083)
### Initializing a resource request
- [init(tags: Set<String>, bundle: Bundle)](./init%28tags,bundle%29.md)
  Initializes a resource request for managing the on-demand resources marked with any of the set of specified tags. The managed resources are loaded into the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/init(tags:))*