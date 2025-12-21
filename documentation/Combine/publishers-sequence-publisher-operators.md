# Publisher Operators

**Framework**: Combine

Methods that create downstream publishers or subscribers to act on the elements they receive.

## Topics

### Mapping elements
- [func map<T>((Elements.Element) -> T) -> Publishers.Sequence<[T], Failure>](publishers/sequence/map(_:).md)
- [func scan<T>(T, (T, Publishers.Sequence<Elements, Failure>.Output) -> T) -> Publishers.Sequence<[T], Failure>](publishers/sequence/scan(_:_:).md)
- [func setFailureType<E>(to: E.Type) -> Publishers.Sequence<Elements, E>](publishers/sequence/setfailuretype(to:).md)
- [func replaceNil<T>(with: T) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](publishers/sequence/replacenil(with:).md)
### Filtering elements
- [func filter((Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](publishers/sequence/filter(_:).md)
- [func compactMap<T>((Publishers.Sequence<Elements, Failure>.Output) -> T?) -> Publishers.Sequence<[T], Failure>](publishers/sequence/compactmap(_:).md)
- [func removeDuplicates() -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](publishers/sequence/removeduplicates.md)
### Reducing elements
- [func collect() -> Result<[Publishers.Sequence<Elements, Failure>.Output], Failure>.Publisher](publishers/sequence/collect.md)
- [func ignoreOutput() -> Empty<Publishers.Sequence<Elements, Failure>.Output, Failure>](publishers/sequence/ignoreoutput.md)
- [func reduce<T>(T, (T, Publishers.Sequence<Elements, Failure>.Output) -> T) -> Result<T, Failure>.Publisher](publishers/sequence/reduce(_:_:).md)
- [func tryReduce<T>(T, (T, Publishers.Sequence<Elements, Failure>.Output) throws -> T) -> Result<T, any Error>.Publisher](publishers/sequence/tryreduce(_:_:).md)
### Applying mathematical operations on elements
- [func count() -> Just<Int>](publishers/sequence/count-5rrw2.md)
- [func count() -> Result<Int, Failure>.Publisher](publishers/sequence/count-5hb52.md)
- [func count() -> Result<Int, Failure>.Publisher](publishers/sequence/count-b8ct.md)
- [func max() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/max.md)
- [func max(by: (Publishers.Sequence<Elements, Failure>.Output, Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/max(by:).md)
- [func min() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/min.md)
- [func min(by: (Publishers.Sequence<Elements, Failure>.Output, Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/min(by:).md)
### Applying matching criteria to elements
- [func contains(Elements.Element) -> Result<Bool, Failure>.Publisher](publishers/sequence/contains(_:).md)
- [func contains(where: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Result<Bool, Failure>.Publisher](publishers/sequence/contains(where:).md)
- [func tryContains(where: (Publishers.Sequence<Elements, Failure>.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](publishers/sequence/trycontains(where:).md)
- [func allSatisfy((Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Result<Bool, Failure>.Publisher](publishers/sequence/allsatisfy(_:).md)
- [func tryAllSatisfy((Publishers.Sequence<Elements, Failure>.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](publishers/sequence/tryallsatisfy(_:).md)
### Applying sequence operations to elements
- [func dropFirst(Int) -> Publishers.Sequence<DropFirstSequence<Elements>, Failure>](publishers/sequence/dropfirst(_:).md)
- [func drop(while: (Elements.Element) -> Bool) -> Publishers.Sequence<DropWhileSequence<Elements>, Failure>](publishers/sequence/drop(while:).md)
- [func append<S>(S) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/append(_:)-45rm8.md)
- [func append(Publishers.Sequence<Elements, Failure>) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/append(_:)-3dj6k.md)
- [func append(Publishers.Sequence<Elements, Failure>.Output...) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/append(_:)-2knh4.md)
- [func prepend<S>(S) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/prepend(_:)-1r564.md)
- [func prepend(Publishers.Sequence<Elements, Failure>) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/prepend(_:)-71f7p.md)
- [func prepend(Publishers.Sequence<Elements, Failure>.Output...) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/prepend(_:)-2ros1.md)
- [func prefix(Int) -> Publishers.Sequence<PrefixSequence<Elements>, Failure>](publishers/sequence/prefix(_:).md)
- [func prefix(while: (Elements.Element) -> Bool) -> Publishers.Sequence<[Elements.Element], Failure>](publishers/sequence/prefix(while:).md)
### Selecting specific elements
- [func first() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/first.md)
- [func first(where: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/first(where:).md)
- [func last() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/last.md)
- [func last(where: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/last(where:).md)
- [func output(at: Elements.Index) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/output(at:)-3r7zo.md)
- [func output(at: Elements.Index) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/output(at:)-9kto7.md)
- [func output(in: Range<Elements.Index>) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](publishers/sequence/output(in:)-6g2zc.md)
- [func output(in: Range<Elements.Index>) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](publishers/sequence/output(in:)-8l6yw.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers-sequence-publisher-operators)*