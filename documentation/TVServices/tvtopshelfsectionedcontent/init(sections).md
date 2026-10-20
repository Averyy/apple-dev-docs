# init(sections:)

**Framework**: TV Services  
**Kind**: init  
**Role**: Initializer

Creates a sectioned content object and populates it with the specified sections.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
init(sections: [TVTopShelfItemCollection<TVTopShelfSectionedItem>])
```

```objc
- (instancetype) initWithSections:(NSArray<TVTopShelfItemCollection<TVTopShelfSectionedItem *> *> *) sections;
```

#### Return Value

A new sectioned content object containing the specified sections.

## Parameters

- `sections`: An array of [`TVTopShelfItemCollection`](../tvtopshelfitemcollection.md) objects, representing the sections of your interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfsectionedcontent/init(sections:))*