# init(readonlyAttributeWithID:initialValue:requiredPrivilege:)

**Framework**: Matter  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
init?(readonlyAttributeWithID attributeID: NSNumber, initialValue value: [String : Any], requiredPrivilege: MTRAccessControlEntryPrivilege)
```

```objc
- (instancetype) initReadonlyAttributeWithID:(NSNumber *) attributeID initialValue:(NSDictionary<NSString *,id> *) value requiredPrivilege:(MTRAccessControlEntryPrivilege) requiredPrivilege;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrserverattribute/init(readonlyattributewithid:initialvalue:requiredprivilege:))*