# kCMTagCollectionTagsArrayKey

**Framework**: Core Media  
**Kind**: var  
**Role**: Global Variable

A dictionary key for assigning tag collections to.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```c
extern CFStringRef const kCMTagCollectionTagsArrayKey;
```

#### Discussion

Avoid creating dictionaries and setting this key yourself. Call [`CMTagCollectionCopyAsDictionary`](./cmtagcollectioncopyasdictionary.md) on an existing, valid tag collection instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtagcollectiontagsarraykey)*