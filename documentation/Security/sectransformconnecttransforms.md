# SecTransformConnectTransforms(_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Chains transforms together.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformConnectTransforms(_ sourceTransformRef: SecTransform, _ sourceAttributeName: CFString, _ destinationTransformRef: SecTransform, _ destinationAttributeName: CFString, _ group: SecGroupTransform, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecGroupTransform?
```

#### Return Value

A [`SecGroupTransform`](secgrouptransform.md) object that you can use for chaining calls to [`SecTransformConnectTransforms(_:_:_:_:_:_:)`](sectransformconnecttransforms(_:_:_:_:_:_:).md).

#### Discussion

This function places transforms into a group by attaching the value of an attribute of one transform to the attribute of another transform. Typically the attribute supplying the data is the kSecTransformAttrOutput attribute but that is not a requirement. It can be used to set an attribute like Salt with the output attribute of a random number transform. This function returns an error and the named attribute will not be changed if [`SecTransformExecute(_:_:)`](sectransformexecute(_:_:).md) had previously been called on the transform.

## Parameters

- `sourceTransformRef`: The transform that sends the data to the destinationTransformRef.
- `sourceAttributeName`: The name of the attribute in the sourceTransformRef that supplies the data to the destinationTransformRef. Any attribute of the transform may be used as a source.
- `destinationTransformRef`: The transform that has one of its attributes be set with the data from the sourceTransformRef parameter.
- `destinationAttributeName`: The name of the attribute within the destinationTransformRef whose data is set with the data from the sourceTransformRef sourceAttributeName attribute. Any attribute of the transform may be set.
- `group`: In the example below, the output of trans1 is set to be the input of trans2. The output of trans2 is set to be the input of trans3. Since the same group was used for the connections, the three transforms are in the same group.
- `error`: An optional pointer to a CFErrorRef. This value is set if an error occurred. If not NULL, the caller is responsible for releasing the CFErrorRef.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformconnecttransforms(_:_:_:_:_:_:))*