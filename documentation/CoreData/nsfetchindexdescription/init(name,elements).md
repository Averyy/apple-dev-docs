# init(name:elements:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Creates a fetch index description using the specified name and element descriptions.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(name: String, elements: [NSFetchIndexElementDescription]?)
```

```objc
- (instancetype) initWithName:(NSString *) name elements:(NSArray<NSFetchIndexElementDescription *> *) elements;
```

## Parameters

- `name`: The name of the fetch index description.
- `elements`: An array of fetch index element descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchindexdescription/init(name:elements:))*