# intentsPercentagePass

**Framework**: Evaluations  
**Kind**: property  
**Role**: Type Property

The fraction of intent expectations that held, for one scenario.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- Xcode 27.0+

## Declaration

```swift
static let intentsPercentagePass: Metric
```

## Discussion

Every `Calls` check counts once, so a `.disallowed` that held counts as much as a required call that ran: a scenario where Siri called nothing can still score high. Gate a test on [`intentsAllPass`](./intentsallpass.md) and read the share as a diagnostic.

The share is shown per scenario and left out of the summary, so `aggregateValue(.mean(of:))` returns -1 for it. Read it from the result’s rows. The column is missing when no scenario was graded, and reading a missing column traps, so check for it first:

```swift
let shares =
    result.detailed.containsColumn(Metric.intentsPercentagePass.name)
    ? result.detailed[metric: .intentsPercentagePass].compactMap { $0?.doubleValue } : []
#expect(result.aggregateValue(.mean(of: .intentsAllPass)) == 1, "Correct Intents: \(shares)")
```

A scenario has no share when it has no intent expectations or when it could not run or be graded, so compare `shares.count` with the number of scenarios you expect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric/intentspercentagepass)*