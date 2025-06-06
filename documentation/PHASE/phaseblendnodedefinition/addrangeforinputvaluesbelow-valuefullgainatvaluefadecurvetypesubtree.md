# addRangeForInputValuesBelow(value:fullGainAtValue:fadeCurveType:subtree:)

**Framework**: PHASE  
**Kind**: method

Adds a child node that blends below a given value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func addRangeForInputValuesBelow(value: Double, fullGainAtValue: Double, fadeCurveType: PHASECurveType, subtree: PHASESoundEventNodeDefinition)
```

## Parameters

- `value`: The value above which the child node blends.
- `fullGainAtValue`: A threshold such that the node applies a fade curve to the child node’s gain when the blend parameter is between   and this value.
- `fadeCurveType`: An option that determines a rate of change for the child node’s gain over the fade range.
- `subtree`: A child node to blend.

## See Also

- [func addRange(envelope: PHASEEnvelope, subtree: PHASESoundEventNodeDefinition)](phaseblendnodedefinition/addrange(envelope:subtree:).md)
  Adds a child node with an envelope.
- [func addRangeForInputValuesAbove(value: Double, fullGainAtValue: Double, fadeCurveType: PHASECurveType, subtree: PHASESoundEventNodeDefinition)](phaseblendnodedefinition/addrangeforinputvaluesabove(value:fullgainatvalue:fadecurvetype:subtree:).md)
  Adds a child node that blends above a given value.
- [func addRangeForInputValuesBetween(lowValue: Double, highValue: Double, fullGainAtLowValue: Double, fullGainAtHighValue: Double, lowFadeCurveType: PHASECurveType, highFadeCurveType: PHASECurveType, subtree: PHASESoundEventNodeDefinition)](phaseblendnodedefinition/addrangeforinputvaluesbetween(lowvalue:highvalue:fullgainatlowvalue:fullgainathighvalue:lowfadecurvetype:highfadecurvetype:subtree:).md)
  Adds a child node that blends between a given high and low value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseblendnodedefinition/addrangeforinputvaluesbelow(value:fullgainatvalue:fadecurvetype:subtree:))*