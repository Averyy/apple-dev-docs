# addRangeForInputValuesBetween(lowValue:highValue:fullGainAtLowValue:fullGainAtHighValue:lowFadeCurveType:highFadeCurveType:subtree:)

**Framework**: PHASE  
**Kind**: method

Adds a child node that blends between a given high and low value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func addRangeForInputValuesBetween(lowValue: Double, highValue: Double, fullGainAtLowValue: Double, fullGainAtHighValue: Double, lowFadeCurveType: PHASECurveType, highFadeCurveType: PHASECurveType, subtree: PHASESoundEventNodeDefinition)
```

## Parameters

- `lowValue`: A value above which the child node blends.
- `highValue`: A value below which the child node blends.
- `fullGainAtLowValue`: The threshold for which a fade curve that   defines applies to the gain when the blend parameter value is between   and  .
- `fullGainAtHighValue`: The threshold for which a fade curve that   defines applies to the gain when the blend parameter value is between   and  .
- `lowFadeCurveType`: An option that determines a rate of change for the child node’s gain over the low fade range.
- `highFadeCurveType`: An option that determines a rate of change for the child node’s gain over the high fade range.
- `subtree`: A child node to blend.

## See Also

- [func addRange(envelope: PHASEEnvelope, subtree: PHASESoundEventNodeDefinition)](phaseblendnodedefinition/addrange(envelope:subtree:).md)
  Adds a child node with an envelope.
- [func addRangeForInputValuesAbove(value: Double, fullGainAtValue: Double, fadeCurveType: PHASECurveType, subtree: PHASESoundEventNodeDefinition)](phaseblendnodedefinition/addrangeforinputvaluesabove(value:fullgainatvalue:fadecurvetype:subtree:).md)
  Adds a child node that blends above a given value.
- [func addRangeForInputValuesBelow(value: Double, fullGainAtValue: Double, fadeCurveType: PHASECurveType, subtree: PHASESoundEventNodeDefinition)](phaseblendnodedefinition/addrangeforinputvaluesbelow(value:fullgainatvalue:fadecurvetype:subtree:).md)
  Adds a child node that blends below a given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseblendnodedefinition/addrangeforinputvaluesbetween(lowvalue:highvalue:fullgainatlowvalue:fullgainathighvalue:lowfadecurvetype:highfadecurvetype:subtree:))*