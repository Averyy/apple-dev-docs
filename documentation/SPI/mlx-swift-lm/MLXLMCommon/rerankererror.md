---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankererror"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RerankerError

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Errors thrown while preparing or scoring reranker inputs.

## Declaration

```swift
enum RerankerError
```

## Topics

### Enumeration Cases
- [RerankerError.classifierTokenIsNotSingleToken(_:_:)](./rerankererror/classifiertokenisnotsingletoken%28_,_%29.md)
- [RerankerError.duplicateDocumentID(_:)](./rerankererror/duplicatedocumentid%28_%29.md)
- [RerankerError.duplicateResultIndex(_:)](./rerankererror/duplicateresultindex%28_%29.md)
- [RerankerError.emptyDocument(index:)](./rerankererror/emptydocument%28index%29.md)
- [RerankerError.emptyPrompt](./rerankererror/emptyprompt.md)
- [RerankerError.emptyQuery](./rerankererror/emptyquery.md)
- [case inputTooLong(actual: Int, maximum: Int)](./rerankererror/inputtoolong%28actual,maximum%29.md)
- [case invalidExecutionOption(name: String, value: Int)](./rerankererror/invalidexecutionoption%28name,value%29.md)
- [RerankerError.invalidLogitShape(_:)](./rerankererror/invalidlogitshape%28_%29.md)
- [case invalidMinimumScore(Double, validRange: ClosedRange<Double>?)](./rerankererror/invalidminimumscore%28_,validrange%29.md)
- [case invalidResultIndex(index: Int, documentCount: Int)](./rerankererror/invalidresultindex%28index,documentcount%29.md)
- [case invalidResultOrder(expected: Int, actual: Int)](./rerankererror/invalidresultorder%28expected,actual%29.md)
- [case invalidScoreCount(expected: Int, actual: Int)](./rerankererror/invalidscorecount%28expected,actual%29.md)
- [RerankerError.invalidTopK(_:)](./rerankererror/invalidtopk%28_%29.md)
- [RerankerError.missingClassifierToken(_:)](./rerankererror/missingclassifiertoken%28_%29.md)
- [RerankerError.missingSpecialToken(_:)](./rerankererror/missingspecialtoken%28_%29.md)
- [case nonFiniteScore(index: Int, score: Double)](./rerankererror/nonfinitescore%28index,score%29.md)
- [case scoreOutOfRange(index: Int, score: Double, range: ClosedRange<Double>)](./rerankererror/scoreoutofrange%28index,score,range%29.md)
- [RerankerError.thresholdUnsupported](./rerankererror/thresholdunsupported.md)
- [case tokenLimitTooSmall(maxInputTokens: Int, requiredTemplateTokens: Int)](./rerankererror/tokenlimittoosmall%28maxinputtokens,requiredtemplatetokens%29.md)
- [case tooManyDocuments(actual: Int, maximum: Int)](./rerankererror/toomanydocuments%28actual,maximum%29.md)
- [RerankerError.truncatedRequiredToken(_:)](./rerankererror/truncatedrequiredtoken%28_%29.md)
- [RerankerError.unsupportedModel(_:)](./rerankererror/unsupportedmodel%28_%29.md)
### Instance Properties
- [var errorDescription: String?](./rerankererror/errordescription.md)
### Default Implementations
- [Error Implementations](./rerankererror/error-implementations.md)
- [LocalizedError Implementations](./rerankererror/localizederror-implementations.md)

## Relationships

### Conforms To
- Foundation.LocalizedError
- Swift.Error
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankererror)*