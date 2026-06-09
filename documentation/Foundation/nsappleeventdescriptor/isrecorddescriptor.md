# isRecordDescriptor

**Framework**: Foundation  
**Kind**: property

Returns whether or not the receiver is a record-like descriptor.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var isRecordDescriptor: Bool { get }
```

#### Discussion

Record-like descriptors function as records, but may have a `descriptorType` other than `typeAERecord`, such as `typeObjectSpecifier`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/isrecorddescriptor)*