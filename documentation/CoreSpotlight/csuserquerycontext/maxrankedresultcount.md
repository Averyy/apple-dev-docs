# maxRankedResultCount

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The maximum number of ranked results to return during the query.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var maxRankedResultCount: Int { get set }
```

```objc
@property (nonatomic, assign) NSInteger maxRankedResultCount;
```

## Discussion

Spotlight ranks a limited number of results by default, but you can change the default value to improve performance or better suit your app’s interface. For example, you might want to return only the five most relevant results due to space constraints in your UI.

## See Also

### Configuring the ranked results behavior
- [var enableRankedResults: Bool](./enablerankedresults.md)
  A Boolean value that indicates whether the query sorts results by their relevance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquerycontext/maxrankedresultcount)*