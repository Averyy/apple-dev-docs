# Atomic

**Framework**: Synchronization  
**Kind**: struct  
**Role**: Structure

An atomic value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@frozen
struct Atomic<Value> where Value : AtomicRepresentable
```

## Topics

### Initializers
- [init(consuming Value)](./atomic/init%28_%29.md)
  Initializes a value of this atomic with the given initial value.
### Instance Methods
- [func add(UInt128, ordering: AtomicUpdateOrdering) -> (oldValue: UInt128, newValue: UInt128)](./atomic/add%28_,ordering%29-1k1sq.md)
  Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [func add(Int16, ordering: AtomicUpdateOrdering) -> (oldValue: Int16, newValue: Int16)](./atomic/add%28_,ordering%29-34u14.md)
  Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [func add(UInt32, ordering: AtomicUpdateOrdering) -> (oldValue: UInt32, newValue: UInt32)](./atomic/add%28_,ordering%29-39vk1.md)
  Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [func add(UInt64, ordering: AtomicUpdateOrdering) -> (oldValue: UInt64, newValue: UInt64)](./atomic/add%28_,ordering%29-4dpjd.md)
  Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [func add(UInt16, ordering: AtomicUpdateOrdering) -> (oldValue: UInt16, newValue: UInt16)](./atomic/add%28_,ordering%29-4ocr0.md)
  Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [func add(Int8, ordering: AtomicUpdateOrdering) -> (oldValue: Int8, newValue: Int8)](./atomic/add%28_,ordering%29-6rhji.md)
  Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [func add(Int64, ordering: AtomicUpdateOrdering) -> (oldValue: Int64, newValue: Int64)](./atomic/add%28_,ordering%29-7ws8q.md)
  Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [func add(UInt8, ordering: AtomicUpdateOrdering) -> (oldValue: UInt8, newValue: UInt8)](./atomic/add%28_,ordering%29-8cc78.md)
  Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [func add(UInt, ordering: AtomicUpdateOrdering) -> (oldValue: UInt, newValue: UInt)](./atomic/add%28_,ordering%29-8xoe3.md)
  Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [func add(Int128, ordering: AtomicUpdateOrdering) -> (oldValue: Int128, newValue: Int128)](./atomic/add%28_,ordering%29-90njk.md)
  Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [func add(Int, ordering: AtomicUpdateOrdering) -> (oldValue: Int, newValue: Int)](./atomic/add%28_,ordering%29-97ilu.md)
  Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [func add(Int32, ordering: AtomicUpdateOrdering) -> (oldValue: Int32, newValue: Int32)](./atomic/add%28_,ordering%29-vm4c.md)
  Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseAnd(UInt128, ordering: AtomicUpdateOrdering) -> (oldValue: UInt128, newValue: UInt128)](./atomic/bitwiseand%28_,ordering%29-1baj3.md)
  Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseAnd(UInt16, ordering: AtomicUpdateOrdering) -> (oldValue: UInt16, newValue: UInt16)](./atomic/bitwiseand%28_,ordering%29-1gzwl.md)
  Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseAnd(Int8, ordering: AtomicUpdateOrdering) -> (oldValue: Int8, newValue: Int8)](./atomic/bitwiseand%28_,ordering%29-1yz1m.md)
  Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseAnd(Int16, ordering: AtomicUpdateOrdering) -> (oldValue: Int16, newValue: Int16)](./atomic/bitwiseand%28_,ordering%29-3zt46.md)
  Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseAnd(Int64, ordering: AtomicUpdateOrdering) -> (oldValue: Int64, newValue: Int64)](./atomic/bitwiseand%28_,ordering%29-4db7m.md)
  Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseAnd(Int128, ordering: AtomicUpdateOrdering) -> (oldValue: Int128, newValue: Int128)](./atomic/bitwiseand%28_,ordering%29-56lhq.md)
  Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseAnd(UInt32, ordering: AtomicUpdateOrdering) -> (oldValue: UInt32, newValue: UInt32)](./atomic/bitwiseand%28_,ordering%29-5iaoz.md)
  Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseAnd(Int, ordering: AtomicUpdateOrdering) -> (oldValue: Int, newValue: Int)](./atomic/bitwiseand%28_,ordering%29-5m0jk.md)
  Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseAnd(UInt, ordering: AtomicUpdateOrdering) -> (oldValue: UInt, newValue: UInt)](./atomic/bitwiseand%28_,ordering%29-5mhgj.md)
  Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseAnd(UInt64, ordering: AtomicUpdateOrdering) -> (oldValue: UInt64, newValue: UInt64)](./atomic/bitwiseand%28_,ordering%29-6mxdg.md)
  Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseAnd(Int32, ordering: AtomicUpdateOrdering) -> (oldValue: Int32, newValue: Int32)](./atomic/bitwiseand%28_,ordering%29-8ilt7.md)
  Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseAnd(UInt8, ordering: AtomicUpdateOrdering) -> (oldValue: UInt8, newValue: UInt8)](./atomic/bitwiseand%28_,ordering%29-l1a3.md)
  Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseOr(Int32, ordering: AtomicUpdateOrdering) -> (oldValue: Int32, newValue: Int32)](./atomic/bitwiseor%28_,ordering%29-206dk.md)
  Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseOr(Int64, ordering: AtomicUpdateOrdering) -> (oldValue: Int64, newValue: Int64)](./atomic/bitwiseor%28_,ordering%29-39r9q.md)
  Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseOr(UInt64, ordering: AtomicUpdateOrdering) -> (oldValue: UInt64, newValue: UInt64)](./atomic/bitwiseor%28_,ordering%29-4ozz5.md)
  Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseOr(UInt8, ordering: AtomicUpdateOrdering) -> (oldValue: UInt8, newValue: UInt8)](./atomic/bitwiseor%28_,ordering%29-4q8ef.md)
  Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseOr(Int128, ordering: AtomicUpdateOrdering) -> (oldValue: Int128, newValue: Int128)](./atomic/bitwiseor%28_,ordering%29-4y864.md)
  Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseOr(UInt128, ordering: AtomicUpdateOrdering) -> (oldValue: UInt128, newValue: UInt128)](./atomic/bitwiseor%28_,ordering%29-5574x.md)
  Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseOr(UInt16, ordering: AtomicUpdateOrdering) -> (oldValue: UInt16, newValue: UInt16)](./atomic/bitwiseor%28_,ordering%29-6fz7a.md)
  Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseOr(UInt, ordering: AtomicUpdateOrdering) -> (oldValue: UInt, newValue: UInt)](./atomic/bitwiseor%28_,ordering%29-6zz2p.md)
  Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseOr(Int, ordering: AtomicUpdateOrdering) -> (oldValue: Int, newValue: Int)](./atomic/bitwiseor%28_,ordering%29-72403.md)
  Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseOr(UInt32, ordering: AtomicUpdateOrdering) -> (oldValue: UInt32, newValue: UInt32)](./atomic/bitwiseor%28_,ordering%29-84e8q.md)
  Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseOr(Int16, ordering: AtomicUpdateOrdering) -> (oldValue: Int16, newValue: Int16)](./atomic/bitwiseor%28_,ordering%29-9191v.md)
  Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseOr(Int8, ordering: AtomicUpdateOrdering) -> (oldValue: Int8, newValue: Int8)](./atomic/bitwiseor%28_,ordering%29-aa7f.md)
  Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseXor(UInt128, ordering: AtomicUpdateOrdering) -> (oldValue: UInt128, newValue: UInt128)](./atomic/bitwisexor%28_,ordering%29-271x9.md)
  Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseXor(Int16, ordering: AtomicUpdateOrdering) -> (oldValue: Int16, newValue: Int16)](./atomic/bitwisexor%28_,ordering%29-2vrf.md)
  Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseXor(UInt32, ordering: AtomicUpdateOrdering) -> (oldValue: UInt32, newValue: UInt32)](./atomic/bitwisexor%28_,ordering%29-33l7y.md)
  Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseXor(Int, ordering: AtomicUpdateOrdering) -> (oldValue: Int, newValue: Int)](./atomic/bitwisexor%28_,ordering%29-4umey.md)
  Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseXor(UInt, ordering: AtomicUpdateOrdering) -> (oldValue: UInt, newValue: UInt)](./atomic/bitwisexor%28_,ordering%29-5df6p.md)
  Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseXor(Int8, ordering: AtomicUpdateOrdering) -> (oldValue: Int8, newValue: Int8)](./atomic/bitwisexor%28_,ordering%29-5vpxh.md)
  Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseXor(UInt16, ordering: AtomicUpdateOrdering) -> (oldValue: UInt16, newValue: UInt16)](./atomic/bitwisexor%28_,ordering%29-5zfc.md)
  Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseXor(Int128, ordering: AtomicUpdateOrdering) -> (oldValue: Int128, newValue: Int128)](./atomic/bitwisexor%28_,ordering%29-8t1qf.md)
  Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseXor(UInt64, ordering: AtomicUpdateOrdering) -> (oldValue: UInt64, newValue: UInt64)](./atomic/bitwisexor%28_,ordering%29-9l5qb.md)
  Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseXor(Int32, ordering: AtomicUpdateOrdering) -> (oldValue: Int32, newValue: Int32)](./atomic/bitwisexor%28_,ordering%29-9xi4f.md)
  Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseXor(UInt8, ordering: AtomicUpdateOrdering) -> (oldValue: UInt8, newValue: UInt8)](./atomic/bitwisexor%28_,ordering%29-m4nt.md)
  Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [func bitwiseXor(Int64, ordering: AtomicUpdateOrdering) -> (oldValue: Int64, newValue: Int64)](./atomic/bitwisexor%28_,ordering%29-sf4i.md)
  Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [func compareExchange(expected: consuming Value, desired: consuming Value, ordering: AtomicUpdateOrdering) -> (exchanged: Bool, original: Value)](./atomic/compareexchange%28expected,desired,ordering%29-33pf3.md)
  Perform an atomic compare and exchange operation on the current value, applying the specified memory ordering.
- [func compareExchange(expected: consuming Value, desired: consuming Value, ordering: AtomicUpdateOrdering) -> (exchanged: Bool, original: Value)](./atomic/compareexchange%28expected,desired,ordering%29-6rsfl.md)
  Perform an atomic compare and exchange operation on the current value, applying the specified memory ordering.
- [func compareExchange(expected: consuming Value, desired: consuming Value, ordering: AtomicUpdateOrdering) -> (exchanged: Bool, original: Value)](./atomic/compareexchange%28expected,desired,ordering%29-8uimm.md)
  Perform an atomic compare and exchange operation on the current value, applying the specified memory ordering.
- [func compareExchange(expected: consuming Value, desired: consuming Value, ordering: AtomicUpdateOrdering) -> (exchanged: Bool, original: Value)](./atomic/compareexchange%28expected,desired,ordering%29-9bh60.md)
  Perform an atomic compare and exchange operation on the current value, applying the specified memory ordering.
- [func compareExchange(expected: consuming Value, desired: consuming Value, ordering: AtomicUpdateOrdering) -> (exchanged: Bool, original: Value)](./atomic/compareexchange%28expected,desired,ordering%29-s52j.md)
  Perform an atomic compare and exchange operation on the current value, applying the specified memory ordering.
- [func compareExchange(expected: consuming Value, desired: consuming Value, successOrdering: AtomicUpdateOrdering, failureOrdering: AtomicLoadOrdering) -> (exchanged: Bool, original: Value)](./atomic/compareexchange%28expected,desired,successordering,failureordering%29-5obt4.md)
  Perform an atomic compare and exchange operation on the current value, applying the specified success/failure memory orderings.
- [func compareExchange(expected: consuming Value, desired: consuming Value, successOrdering: AtomicUpdateOrdering, failureOrdering: AtomicLoadOrdering) -> (exchanged: Bool, original: Value)](./atomic/compareexchange%28expected,desired,successordering,failureordering%29-7msfy.md)
  Perform an atomic compare and exchange operation on the current value, applying the specified success/failure memory orderings.
- [func compareExchange(expected: consuming Value, desired: consuming Value, successOrdering: AtomicUpdateOrdering, failureOrdering: AtomicLoadOrdering) -> (exchanged: Bool, original: Value)](./atomic/compareexchange%28expected,desired,successordering,failureordering%29-82j0l.md)
  Perform an atomic compare and exchange operation on the current value, applying the specified success/failure memory orderings.
- [func compareExchange(expected: consuming Value, desired: consuming Value, successOrdering: AtomicUpdateOrdering, failureOrdering: AtomicLoadOrdering) -> (exchanged: Bool, original: Value)](./atomic/compareexchange%28expected,desired,successordering,failureordering%29-8d36a.md)
  Perform an atomic compare and exchange operation on the current value, applying the specified success/failure memory orderings.
- [func compareExchange(expected: consuming Value, desired: consuming Value, successOrdering: AtomicUpdateOrdering, failureOrdering: AtomicLoadOrdering) -> (exchanged: Bool, original: Value)](./atomic/compareexchange%28expected,desired,successordering,failureordering%29-cve0.md)
  Perform an atomic compare and exchange operation on the current value, applying the specified success/failure memory orderings.
- [func exchange(consuming Value, ordering: AtomicUpdateOrdering) -> Value](./atomic/exchange%28_,ordering%29-5n6sy.md)
  Atomically sets the current value to `desired` and returns the original value, applying the specified memory ordering.
- [func exchange(consuming Value, ordering: AtomicUpdateOrdering) -> Value](./atomic/exchange%28_,ordering%29-8ip0d.md)
  Atomically sets the current value to `desired` and returns the original value, applying the specified memory ordering.
- [func exchange(consuming Value, ordering: AtomicUpdateOrdering) -> Value](./atomic/exchange%28_,ordering%29-9kb4s.md)
  Atomically sets the current value to `desired` and returns the original value, applying the specified memory ordering.
- [func exchange(consuming Value, ordering: AtomicUpdateOrdering) -> Value](./atomic/exchange%28_,ordering%29-9y5j8.md)
  Atomically sets the current value to `desired` and returns the original value, applying the specified memory ordering.
- [func exchange(consuming Value, ordering: AtomicUpdateOrdering) -> Value](./atomic/exchange%28_,ordering%29-ycta.md)
  Atomically sets the current value to `desired` and returns the original value, applying the specified memory ordering.
- [func load(ordering: AtomicLoadOrdering) -> Value](./atomic/load%28ordering%29-2u27y.md)
  Atomically loads and returns the current value, applying the specified memory ordering.
- [func load(ordering: AtomicLoadOrdering) -> Value](./atomic/load%28ordering%29-2v8gp.md)
  Atomically loads and returns the current value, applying the specified memory ordering.
- [func load(ordering: AtomicLoadOrdering) -> Value](./atomic/load%28ordering%29-3u18o.md)
  Atomically loads and returns the current value, applying the specified memory ordering.
- [func load(ordering: AtomicLoadOrdering) -> Value](./atomic/load%28ordering%29-4mv5b.md)
  Atomically loads and returns the current value, applying the specified memory ordering.
- [func load(ordering: AtomicLoadOrdering) -> Value](./atomic/load%28ordering%29-8ufx2.md)
  Atomically loads and returns the current value, applying the specified memory ordering.
- [func logicalAnd(Bool, ordering: AtomicUpdateOrdering) -> (oldValue: Bool, newValue: Bool)](./atomic/logicaland%28_,ordering%29.md)
  Perform an atomic logical AND operation and return the old and new value, applying the specified memory ordering.
- [func logicalOr(Bool, ordering: AtomicUpdateOrdering) -> (oldValue: Bool, newValue: Bool)](./atomic/logicalor%28_,ordering%29.md)
  Perform an atomic logical OR operation and return the old and new value, applying the specified memory ordering.
- [func logicalXor(Bool, ordering: AtomicUpdateOrdering) -> (oldValue: Bool, newValue: Bool)](./atomic/logicalxor%28_,ordering%29.md)
  Perform an atomic logical XOR operation and return the old and new value, applying the specified memory ordering.
- [func max(Int16, ordering: AtomicUpdateOrdering) -> (oldValue: Int16, newValue: Int16)](./atomic/max%28_,ordering%29-1l8lv.md)
  Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [func max(UInt, ordering: AtomicUpdateOrdering) -> (oldValue: UInt, newValue: UInt)](./atomic/max%28_,ordering%29-32cin.md)
  Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [func max(Int128, ordering: AtomicUpdateOrdering) -> (oldValue: Int128, newValue: Int128)](./atomic/max%28_,ordering%29-4e4mn.md)
  Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [func max(Int64, ordering: AtomicUpdateOrdering) -> (oldValue: Int64, newValue: Int64)](./atomic/max%28_,ordering%29-4rq6h.md)
  Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [func max(UInt128, ordering: AtomicUpdateOrdering) -> (oldValue: UInt128, newValue: UInt128)](./atomic/max%28_,ordering%29-5qqv7.md)
  Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [func max(UInt64, ordering: AtomicUpdateOrdering) -> (oldValue: UInt64, newValue: UInt64)](./atomic/max%28_,ordering%29-681q1.md)
  Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [func max(Int32, ordering: AtomicUpdateOrdering) -> (oldValue: Int32, newValue: Int32)](./atomic/max%28_,ordering%29-7kusb.md)
  Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [func max(UInt32, ordering: AtomicUpdateOrdering) -> (oldValue: UInt32, newValue: UInt32)](./atomic/max%28_,ordering%29-7qnkd.md)
  Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [func max(UInt8, ordering: AtomicUpdateOrdering) -> (oldValue: UInt8, newValue: UInt8)](./atomic/max%28_,ordering%29-7z7ub.md)
  Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [func max(Int, ordering: AtomicUpdateOrdering) -> (oldValue: Int, newValue: Int)](./atomic/max%28_,ordering%29-81jab.md)
  Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [func max(UInt16, ordering: AtomicUpdateOrdering) -> (oldValue: UInt16, newValue: UInt16)](./atomic/max%28_,ordering%29-957na.md)
  Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [func max(Int8, ordering: AtomicUpdateOrdering) -> (oldValue: Int8, newValue: Int8)](./atomic/max%28_,ordering%29-xy7u.md)
  Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [func min(Int, ordering: AtomicUpdateOrdering) -> (oldValue: Int, newValue: Int)](./atomic/min%28_,ordering%29-1uwzs.md)
  Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [func min(UInt64, ordering: AtomicUpdateOrdering) -> (oldValue: UInt64, newValue: UInt64)](./atomic/min%28_,ordering%29-2l64c.md)
  Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [func min(Int32, ordering: AtomicUpdateOrdering) -> (oldValue: Int32, newValue: Int32)](./atomic/min%28_,ordering%29-39r27.md)
  Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [func min(UInt8, ordering: AtomicUpdateOrdering) -> (oldValue: UInt8, newValue: UInt8)](./atomic/min%28_,ordering%29-3tiyt.md)
  Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [func min(UInt128, ordering: AtomicUpdateOrdering) -> (oldValue: UInt128, newValue: UInt128)](./atomic/min%28_,ordering%29-3tk2x.md)
  Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [func min(UInt32, ordering: AtomicUpdateOrdering) -> (oldValue: UInt32, newValue: UInt32)](./atomic/min%28_,ordering%29-4b62m.md)
  Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [func min(Int64, ordering: AtomicUpdateOrdering) -> (oldValue: Int64, newValue: Int64)](./atomic/min%28_,ordering%29-4wv9d.md)
  Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [func min(Int128, ordering: AtomicUpdateOrdering) -> (oldValue: Int128, newValue: Int128)](./atomic/min%28_,ordering%29-6bbf1.md)
  Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [func min(Int16, ordering: AtomicUpdateOrdering) -> (oldValue: Int16, newValue: Int16)](./atomic/min%28_,ordering%29-6ivky.md)
  Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [func min(Int8, ordering: AtomicUpdateOrdering) -> (oldValue: Int8, newValue: Int8)](./atomic/min%28_,ordering%29-73283.md)
  Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [func min(UInt16, ordering: AtomicUpdateOrdering) -> (oldValue: UInt16, newValue: UInt16)](./atomic/min%28_,ordering%29-8k42m.md)
  Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [func min(UInt, ordering: AtomicUpdateOrdering) -> (oldValue: UInt, newValue: UInt)](./atomic/min%28_,ordering%29-yogw.md)
  Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [func store(consuming Value, ordering: AtomicStoreOrdering)](./atomic/store%28_,ordering%29-195np.md)
  Atomically sets the current value to `desired`, applying the specified memory ordering.
- [func store(consuming Value, ordering: AtomicStoreOrdering)](./atomic/store%28_,ordering%29-22zxw.md)
  Atomically sets the current value to `desired`, applying the specified memory ordering.
- [func store(consuming Value, ordering: AtomicStoreOrdering)](./atomic/store%28_,ordering%29-532ut.md)
  Atomically sets the current value to `desired`, applying the specified memory ordering.
- [func store(consuming Value, ordering: AtomicStoreOrdering)](./atomic/store%28_,ordering%29-5q2fi.md)
  Atomically sets the current value to `desired`, applying the specified memory ordering.
- [func store(consuming Value, ordering: AtomicStoreOrdering)](./atomic/store%28_,ordering%29-97ua7.md)
  Atomically sets the current value to `desired`, applying the specified memory ordering.
- [func subtract(UInt128, ordering: AtomicUpdateOrdering) -> (oldValue: UInt128, newValue: UInt128)](./atomic/subtract%28_,ordering%29-1atf4.md)
  Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [func subtract(Int, ordering: AtomicUpdateOrdering) -> (oldValue: Int, newValue: Int)](./atomic/subtract%28_,ordering%29-1iop7.md)
  Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [func subtract(Int128, ordering: AtomicUpdateOrdering) -> (oldValue: Int128, newValue: Int128)](./atomic/subtract%28_,ordering%29-2ddui.md)
  Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [func subtract(UInt64, ordering: AtomicUpdateOrdering) -> (oldValue: UInt64, newValue: UInt64)](./atomic/subtract%28_,ordering%29-2ds2s.md)
  Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [func subtract(UInt32, ordering: AtomicUpdateOrdering) -> (oldValue: UInt32, newValue: UInt32)](./atomic/subtract%28_,ordering%29-3c2nm.md)
  Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [func subtract(Int8, ordering: AtomicUpdateOrdering) -> (oldValue: Int8, newValue: Int8)](./atomic/subtract%28_,ordering%29-47p0x.md)
  Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [func subtract(UInt8, ordering: AtomicUpdateOrdering) -> (oldValue: UInt8, newValue: UInt8)](./atomic/subtract%28_,ordering%29-5rq0s.md)
  Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [func subtract(UInt16, ordering: AtomicUpdateOrdering) -> (oldValue: UInt16, newValue: UInt16)](./atomic/subtract%28_,ordering%29-65sge.md)
  Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [func subtract(Int64, ordering: AtomicUpdateOrdering) -> (oldValue: Int64, newValue: Int64)](./atomic/subtract%28_,ordering%29-6eidf.md)
  Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [func subtract(Int32, ordering: AtomicUpdateOrdering) -> (oldValue: Int32, newValue: Int32)](./atomic/subtract%28_,ordering%29-7ebxd.md)
  Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [func subtract(Int16, ordering: AtomicUpdateOrdering) -> (oldValue: Int16, newValue: Int16)](./atomic/subtract%28_,ordering%29-9w06o.md)
  Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [func subtract(UInt, ordering: AtomicUpdateOrdering) -> (oldValue: UInt, newValue: UInt)](./atomic/subtract%28_,ordering%29-pqxe.md)
  Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [func weakCompareExchange(expected: consuming Value, desired: consuming Value, ordering: AtomicUpdateOrdering) -> (exchanged: Bool, original: Value)](./atomic/weakcompareexchange%28expected,desired,ordering%29-24bnb.md)
  Perform an atomic weak compare and exchange operation on the current value, applying the memory ordering. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [func weakCompareExchange(expected: consuming Value, desired: consuming Value, ordering: AtomicUpdateOrdering) -> (exchanged: Bool, original: Value)](./atomic/weakcompareexchange%28expected,desired,ordering%29-728eh.md)
  Perform an atomic weak compare and exchange operation on the current value, applying the memory ordering. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [func weakCompareExchange(expected: consuming Value, desired: consuming Value, ordering: AtomicUpdateOrdering) -> (exchanged: Bool, original: Value)](./atomic/weakcompareexchange%28expected,desired,ordering%29-72wpg.md)
  Perform an atomic weak compare and exchange operation on the current value, applying the memory ordering. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [func weakCompareExchange(expected: consuming Value, desired: consuming Value, ordering: AtomicUpdateOrdering) -> (exchanged: Bool, original: Value)](./atomic/weakcompareexchange%28expected,desired,ordering%29-9w8ty.md)
  Perform an atomic weak compare and exchange operation on the current value, applying the memory ordering. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [func weakCompareExchange(expected: consuming Value, desired: consuming Value, ordering: AtomicUpdateOrdering) -> (exchanged: Bool, original: Value)](./atomic/weakcompareexchange%28expected,desired,ordering%29-9xqnl.md)
  Perform an atomic weak compare and exchange operation on the current value, applying the memory ordering. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [func weakCompareExchange(expected: consuming Value, desired: consuming Value, successOrdering: AtomicUpdateOrdering, failureOrdering: AtomicLoadOrdering) -> (exchanged: Bool, original: Value)](./atomic/weakcompareexchange%28expected,desired,successordering,failureordering%29-2ywaz.md)
  Perform an atomic weak compare and exchange operation on the current value, applying the specified success/failure memory orderings. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [func weakCompareExchange(expected: consuming Value, desired: consuming Value, successOrdering: AtomicUpdateOrdering, failureOrdering: AtomicLoadOrdering) -> (exchanged: Bool, original: Value)](./atomic/weakcompareexchange%28expected,desired,successordering,failureordering%29-3p8t6.md)
  Perform an atomic weak compare and exchange operation on the current value, applying the specified success/failure memory orderings. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [func weakCompareExchange(expected: consuming Value, desired: consuming Value, successOrdering: AtomicUpdateOrdering, failureOrdering: AtomicLoadOrdering) -> (exchanged: Bool, original: Value)](./atomic/weakcompareexchange%28expected,desired,successordering,failureordering%29-7vtyo.md)
  Perform an atomic weak compare and exchange operation on the current value, applying the specified success/failure memory orderings. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [func weakCompareExchange(expected: consuming Value, desired: consuming Value, successOrdering: AtomicUpdateOrdering, failureOrdering: AtomicLoadOrdering) -> (exchanged: Bool, original: Value)](./atomic/weakcompareexchange%28expected,desired,successordering,failureordering%29-9kx2t.md)
  Perform an atomic weak compare and exchange operation on the current value, applying the specified success/failure memory orderings. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [func weakCompareExchange(expected: consuming Value, desired: consuming Value, successOrdering: AtomicUpdateOrdering, failureOrdering: AtomicLoadOrdering) -> (exchanged: Bool, original: Value)](./atomic/weakcompareexchange%28expected,desired,successordering,failureordering%29-kfa8.md)
  Perform an atomic weak compare and exchange operation on the current value, applying the specified success/failure memory orderings. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [func wrappingAdd(UInt16, ordering: AtomicUpdateOrdering) -> (oldValue: UInt16, newValue: UInt16)](./atomic/wrappingadd%28_,ordering%29-1cynr.md)
  Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [func wrappingAdd(UInt64, ordering: AtomicUpdateOrdering) -> (oldValue: UInt64, newValue: UInt64)](./atomic/wrappingadd%28_,ordering%29-35sou.md)
  Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [func wrappingAdd(Int, ordering: AtomicUpdateOrdering) -> (oldValue: Int, newValue: Int)](./atomic/wrappingadd%28_,ordering%29-3ihte.md)
  Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [func wrappingAdd(Int128, ordering: AtomicUpdateOrdering) -> (oldValue: Int128, newValue: Int128)](./atomic/wrappingadd%28_,ordering%29-3ltc9.md)
  Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [func wrappingAdd(Int32, ordering: AtomicUpdateOrdering) -> (oldValue: Int32, newValue: Int32)](./atomic/wrappingadd%28_,ordering%29-4da1i.md)
  Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [func wrappingAdd(Int8, ordering: AtomicUpdateOrdering) -> (oldValue: Int8, newValue: Int8)](./atomic/wrappingadd%28_,ordering%29-7flp6.md)
  Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [func wrappingAdd(UInt128, ordering: AtomicUpdateOrdering) -> (oldValue: UInt128, newValue: UInt128)](./atomic/wrappingadd%28_,ordering%29-8rrye.md)
  Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [func wrappingAdd(Int16, ordering: AtomicUpdateOrdering) -> (oldValue: Int16, newValue: Int16)](./atomic/wrappingadd%28_,ordering%29-8wun9.md)
  Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [func wrappingAdd(UInt32, ordering: AtomicUpdateOrdering) -> (oldValue: UInt32, newValue: UInt32)](./atomic/wrappingadd%28_,ordering%29-9ce27.md)
  Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [func wrappingAdd(UInt, ordering: AtomicUpdateOrdering) -> (oldValue: UInt, newValue: UInt)](./atomic/wrappingadd%28_,ordering%29-bmso.md)
  Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [func wrappingAdd(Int64, ordering: AtomicUpdateOrdering) -> (oldValue: Int64, newValue: Int64)](./atomic/wrappingadd%28_,ordering%29-u8d5.md)
  Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [func wrappingAdd(UInt8, ordering: AtomicUpdateOrdering) -> (oldValue: UInt8, newValue: UInt8)](./atomic/wrappingadd%28_,ordering%29-ussb.md)
  Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [func wrappingSubtract(Int16, ordering: AtomicUpdateOrdering) -> (oldValue: Int16, newValue: Int16)](./atomic/wrappingsubtract%28_,ordering%29-1bgvk.md)
  Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [func wrappingSubtract(Int64, ordering: AtomicUpdateOrdering) -> (oldValue: Int64, newValue: Int64)](./atomic/wrappingsubtract%28_,ordering%29-3795w.md)
  Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [func wrappingSubtract(UInt128, ordering: AtomicUpdateOrdering) -> (oldValue: UInt128, newValue: UInt128)](./atomic/wrappingsubtract%28_,ordering%29-43111.md)
  Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [func wrappingSubtract(Int, ordering: AtomicUpdateOrdering) -> (oldValue: Int, newValue: Int)](./atomic/wrappingsubtract%28_,ordering%29-6g9gv.md)
  Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [func wrappingSubtract(Int8, ordering: AtomicUpdateOrdering) -> (oldValue: Int8, newValue: Int8)](./atomic/wrappingsubtract%28_,ordering%29-6xyiw.md)
  Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [func wrappingSubtract(UInt32, ordering: AtomicUpdateOrdering) -> (oldValue: UInt32, newValue: UInt32)](./atomic/wrappingsubtract%28_,ordering%29-6y8r7.md)
  Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [func wrappingSubtract(UInt, ordering: AtomicUpdateOrdering) -> (oldValue: UInt, newValue: UInt)](./atomic/wrappingsubtract%28_,ordering%29-7136k.md)
  Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [func wrappingSubtract(UInt64, ordering: AtomicUpdateOrdering) -> (oldValue: UInt64, newValue: UInt64)](./atomic/wrappingsubtract%28_,ordering%29-7203n.md)
  Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [func wrappingSubtract(Int128, ordering: AtomicUpdateOrdering) -> (oldValue: Int128, newValue: Int128)](./atomic/wrappingsubtract%28_,ordering%29-7k1nk.md)
  Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [func wrappingSubtract(UInt8, ordering: AtomicUpdateOrdering) -> (oldValue: UInt8, newValue: UInt8)](./atomic/wrappingsubtract%28_,ordering%29-83zzr.md)
  Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [func wrappingSubtract(UInt16, ordering: AtomicUpdateOrdering) -> (oldValue: UInt16, newValue: UInt16)](./atomic/wrappingsubtract%28_,ordering%29-8o6j2.md)
  Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [func wrappingSubtract(Int32, ordering: AtomicUpdateOrdering) -> (oldValue: Int32, newValue: Int32)](./atomic/wrappingsubtract%28_,ordering%29-8xrpg.md)
  Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Atomic Values
- [struct AtomicLazyReference](./atomiclazyreference.md)
  A lazily initializable atomic strong reference.
- [struct WordPair](./wordpair.md)
  A pair of two word sized `UInt`s.
- [protocol AtomicRepresentable](./atomicrepresentable.md)
  A type that supports atomic operations through a separate atomic storage representation.
- [protocol AtomicOptionalRepresentable](./atomicoptionalrepresentable.md)
  An atomic value that also supports atomic operations when wrapped in an `Optional`. Atomic optional representable types come with a standalone atomic representation for their optional-wrapped variants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomic)*