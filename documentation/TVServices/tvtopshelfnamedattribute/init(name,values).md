# init(name:values:)

**Framework**: TV Services  
**Kind**: init  
**Role**: Initializer

Creates a new named attribute object with the specified values.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
init(name: String, values: [String])
```

```objc
- (instancetype) initWithName:(NSString *) name values:(NSArray<NSString *> *) values;
```

## Return Value

A new named attribute object.

## Parameters

- `name`: The localized name of the attribute.
- `values`: An array of strings containing the attribute values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfnamedattribute/init(name:values:))*