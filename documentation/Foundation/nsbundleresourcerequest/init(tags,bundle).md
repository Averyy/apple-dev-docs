# init(tags:bundle:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a resource request for managing the on-demand resources marked with any of the set of specified tags. The managed resources are loaded into the specified bundle.

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
init(tags: Set<String>, bundle: Bundle)
```

```objc
- (instancetype) initWithTags:(NSSet<NSString *> *) tags bundle:(NSBundle *) bundle;
```

#### Return Value

The initialized resource request.

## Parameters

- `tags`: A set of strings, with each string specifying a tag assigned to resources stored in `bundle`. The value must not be `nil`.
- `bundle`: The bundle used to store the loaded resources. Pass `nil` for the main bundle. The bundle must be the same as the one used in the Xcode project for all the resources marked with the specified tags.

## See Also

### Initializing a resource request
- [convenience init(tags: Set<String>)](./init%28tags%29.md)
  Initializes a resource request for managing the on-demand resources marked with any of the set of specified tags. The managed resources are loaded into the main bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/init(tags:bundle:))*