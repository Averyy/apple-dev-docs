# defaultContainerIdentifier()

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

Returns the identifier of the default container.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func defaultContainerIdentifier() -> String
```

```objc
- (NSString *) defaultContainerIdentifier;
```

#### Return Value

The identifier of the default container.

#### Discussion

This identifier can be used to fetch a default container. A default container is where the user wants new contacts to be added implicitly.

## See Also

### Fetching groups and containers
- [func groups(matching: NSPredicate?) throws -> [CNGroup]](./groups%28matching%29.md)
  Fetches all groups matching the specified predicate.
- [func containers(matching: NSPredicate?) throws -> [CNContainer]](./containers%28matching%29.md)
  Fetches all containers matching the specified predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactstore/defaultcontaineridentifier())*