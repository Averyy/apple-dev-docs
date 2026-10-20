# EntityProperty

**Framework**: App Intents  
**Kind**: class  
**Role**: Class

A property wrapper that exposes the associated property to the system.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
@propertyWrapper
final class EntityProperty<Value> where Value : _IntentValue, Value : Sendable
```

## Mentions

- [Defining app entities for your custom data types](./defining-app-entities-for-your-custom-data-types.md)

## Topics

### Initializers
- [convenience init()](./entityproperty/init%28%29-1rgp4.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-24wv7.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-2eq1j.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-2gbo1.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-2rc7b.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-31od.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-368si.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-3aobi.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-3e3go.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-3tdgm.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-43hzm.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-47d6o.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-5449c.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-59zl1.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-5d6mq.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-5l6yd.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-5rjfx.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-5zbw9.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-5zvby.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-6bimh.md)
  Creates an app intent entity property.
- [convenience init<Entity>()](./entityproperty/init%28%29-6cx8f.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-6h3h5.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-6n7nc.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-6vna5.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-6yx3a.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-7ebfu.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-7ix0k.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-7uz5g.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-7wcbj.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-83wqy.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-8559a.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-85ux9.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-86h4g.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-8k8p6.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-8kijp.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-923hj.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-93vj2.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-97rm5.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-9h9cx.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-9ojq1.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-ci85.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-f4cd.md)
- [convenience init()](./entityproperty/init%28%29-q8rw.md)
  Creates an app intent entity property.
- [convenience init()](./entityproperty/init%28%29-zez4.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-1n2f3.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-1tre8.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-2g2gf.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-2yy7v.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-3bkqh.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-3gx88.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-3jtfe.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-3u0y3.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-3vwb5.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-49w23.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-4edf8.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-4hzv0.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-4v4go.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-4vbp8.md)
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-502qd.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-5ccof.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-5snly.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-5sos9.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-5ua4c.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-5x8sy.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-5zyp8.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-654jt.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-677j5.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-6kbjo.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-6srk9.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-7gl1i.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-7lok5.md)
  Creates an app intent entity property.
- [convenience init<Entity>(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-7potr.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-7wbi.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-7z0du.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-8ju0q.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-914o3.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-940cv.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-97gbv.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-9ftku.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-9xbzc.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-fw6i.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-g4g4.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-ko6r.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-pgtj.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-s36s.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-s54t.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-vg7q.md)
  Creates an app intent entity property.
- [convenience init(customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28customindexingkey%29-zy6u.md)
  Creates an app intent entity property.
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-145bu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-18sy7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-1a528.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-1a8ak.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-1hhi9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-2de4j.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-2jt43.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-2ys0i.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-35vfa.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-372ob.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-3bzjn.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-3ntmn.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-3ri7p.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-3wkd0.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-41ihl.md)
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-4fuf2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-4x4va.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-4xmpx.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-58ntp.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-5g7nv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-5tkms.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-62b1k.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-6r7ne.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-6z647.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-70my4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-71coi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-73wr9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-7aauq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-7dc9c.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-7pjrs.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-7s2an.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-80ad4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-81k0c.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-82pvf.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-8rbz8.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-8weqi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-90x0x.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-9ja6j.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-9sqv6.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-dccd.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String)](./entityproperty/init%28identifier%29-jysj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-otqs.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-pk2s.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String)](./entityproperty/init%28identifier%29-yejc.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-11ojg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-142p3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-14u70.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-20ix9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-2sf95.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-2v9yk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-32j81.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-3e0tb.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-3uk2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-3yqt4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-3yr4d.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-44nj4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-4bzxa.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-4cnpk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-4qmf2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-4szmj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-4ug9l.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-4w5mh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-4zsk5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-5eiyw.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-5fs2j.md)
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-5uh4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-5xzle.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-6dcc7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-72pwy.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-733qo.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-7o3vr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-7ot5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-7wd24.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-7xf6.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-7z385.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-89hin.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-8fnw3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-8oegi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-8y7ig.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-92os3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-9byuj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-9i943.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-9icyi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-9t9w2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-dk9y.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-jro2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-qhmt.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,asyncgetter%29-twzl.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-19ts7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-1d77j.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-1ga6w.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-1kf44.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-1te6v.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-2du0v.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-2jruh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-2txuv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-32nld.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-336th.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-36xvw.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-3bd2t.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-3j04j.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-42jxe.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-45sbt.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-4axu1.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-4kau5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-4wqds.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-5aiat.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-5nh3n.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-5rzfm.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-5vb8j.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-5w5f4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-61idq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-6c58.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-6jcht.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-6qym5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-6uofu.md)
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-7057t.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-70tkw.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-74d4m.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-7j6bw.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-7rl2n.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-921l8.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-9626k.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-96lm9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-9q91x.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-9tq4f.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-9z3yp.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-dr8c.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-dz25.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-khpz.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-p78n.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,customindexingkey%29-y5yt.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-10dhr.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-1pxun.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-1ypy0.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-2hbx8.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-2jjte.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-2q99h.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-2yrfj.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-2zag2.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-3cksp.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-3j6rz.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-3wwam.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-4m45o.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-4taxi.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-4yz3e.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-5fr47.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-5g7a2.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-5jo0r.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-5lgp5.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-5oks3.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-5v6o5.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-5wwp6.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-67rp0.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-69nnr.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-6g6ok.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-6kgke.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-6l706.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-6np1z.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-6pr9n.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-6uosv.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-6xpqy.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-70bzy.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-7fwr7.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-7r8ri.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-7sify.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-7xxut.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-8c8q3.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-8lr1g.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-8mxd5.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-9okes.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-iyug.md)
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-jk1j.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-ti50.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-x4uf.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,customindexingkey,asyncgetter%29-zfbo.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-1n0oq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-2317s.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-23k7u.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-27k7b.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-2ykkq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-30yhq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-38xi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-3pu07.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-3rulq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-3xrlr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-4318r.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-49qlm.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-4mri2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-4nj4l.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-4t2vl.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-5f8ak.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-5sle0.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-5xvlp.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-6cvfv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-6gjra.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-6h3bp.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-6hvuo.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-6u9yf.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-6wsdg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-6x3kk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-73vgv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-77xq8.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-7gq4a.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-7hl94.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-7kcu5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-7n85o.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-7pvov.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-7vfp0.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-7x0e7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-84f3m.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-8lsws.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-8tt6x.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-97aj9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-9fdoc.md)
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-9pu9i.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-ned6.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-opaz.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-pt9d.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getsetter%29-rx4y.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-1ivkd.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-1rw79.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-22bk5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-26ofq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-28x8v.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-2cu5r.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-2ehoe.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-2h1at.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-2mudq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-2v38i.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-2xdb9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-2xqs6.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-31xxq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-32h54.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-32mgg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-38c7x.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-3dvry.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-3erdy.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-3ptx0.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-41g7k.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-48kwr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-4gyqk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-4qreq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-570s4.md)
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-5qhvl.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-61uur.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-66ofu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-6aopq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-6lxh6.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-6uasv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-71o75.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-7c84a.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-7nasr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-7utjm.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-7yufv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-83v5n.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-8fpuh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-8s3pk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-8smyb.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-93qu4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-9lb9p.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-9zett.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-whqs.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,customindexingkey,getter%29-yu6b.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-16a1n.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-1gtdt.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-1jk73.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-2b0xh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-2fhr8.md)
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-2qe1n.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-3h7qr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-3hxqq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-3k39r.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-46kzs.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-4sxe9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-4xbgo.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-52abc.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-5evqj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-5gloc.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-5jkkc.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-5jta5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-5rdkq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-6aix5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-6iakp.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-6ksua.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-6q12y.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-7398m.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-779v3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-795az.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-7a7li.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-7es1q.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-7gjvq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-7gl7g.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-7s3ov.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-8bu81.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-8iank.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-8mxm2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-8vhf9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-90fzj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-9dcdj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-9f3eu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-9j5vw.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-9suqv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-9w9av.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-cbr9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-epfk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-riag.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,getsetter%29-ty5a.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-10ynr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-139qa.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-1yuxg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-25lyv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-29zo4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-2so4z.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-303m7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-33eup.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-3arpe.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-3vrbj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-48e8p.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-4dd82.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-4dx0j.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-4sry9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-4vigz.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-5v2e2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-6j0zg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-756yu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-7az66.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-7ibgv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-7vhil.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-7xein.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-7yd6h.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-829qh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-8a1d3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-8ebf0.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-8fpb3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-8gy65.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-8or16.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-8ztp9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-996ei.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-9b7ss.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-9jv23.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-9l41i.md)
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-9nw7u.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-9ufj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-9v73j.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-9ydos.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-bhjd.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-ccpx.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-i9x.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-ngvd.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-qzcb.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,getter%29-tjgu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-108rt.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-11apu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-1gkg3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-1il4f.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-1nfql.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-2ddlr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-2lc2s.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-2u9sg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-3kwk8.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-3mqqx.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-3oziq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-42bxu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-4aeh2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-53b7s.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-54nfj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-55ots.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-5cblq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-5f29o.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-5kut4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-5n8ae.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-5qczm.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-5rxof.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-5wr9o.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-65jpb.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-6ushp.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-71upj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-79ep6.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-7fy5y.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-7i0i9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-7qdhm.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-7u2ie.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-89dlx.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-8bkuw.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-8pndc.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-8vhty.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-90s7c.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-91n72.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-9ah6u.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-9i6fd.md)
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-9mxx2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-9pfu4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-s9mb.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-tf9i.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,indexingkey%29-yfhp.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-15xu3.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-189da.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-1kjm6.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-1kzd9.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-1xeaq.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-232m6.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-2d7ml.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-2must.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-2ppo3.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-2sdck.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-359z7.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-366jr.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-3euy7.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-3gan8.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-3wq4t.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-41532.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-44nxe.md)
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-49f2f.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-4ir0a.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-4t8po.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-4wn7q.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-5f8rx.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-5jt9t.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-5k1sx.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-5yj31.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-61ver.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-63290.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-6gap0.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-6kakg.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-6kmt5.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-6z5rn.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-720b8.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-7bhda.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-7s9bd.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-80q9.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-83j8b.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-87i5n.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-8c2z8.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-9npjb.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-9qktf.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-b2o.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-guyj.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-hkq5.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,indexingkey,asyncgetter%29-l6at.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-1b00k.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-1bdxp.md)
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-1mbwl.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-1rsr3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-1vtdh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-1x9ef.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-285rk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-29jby.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-2kea8.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-2pt7d.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-3brlp.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-3hxwp.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-3jd1p.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-3sshm.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-3ul3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-49dre.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-4aslb.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-4h3w5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-4qxfy.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-4t8ni.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-4tip7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-4w1uh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-5dfbz.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-5dg1t.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-5fowl.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-5mtpi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-5nzpa.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-5qr3z.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-5r2ir.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-5spbu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-69ehg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-76a5a.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-7xppg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-7zhfg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-84ckj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-889of.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-8hybh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-8xx5f.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-960o7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-9clc3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-9h77.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-gbh3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-k5hw.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getsetter%29-kevb.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-12392.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-16q99.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-1d1rt.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-1fle2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-1uamg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-2235c.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-2385f.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-2745q.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-27q8s.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-2nq08.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-2x7h9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-363er.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-3dfoi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-3ulk0.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-4m36j.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-5b6fs.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-5bqr6.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-5coag.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-5qeof.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-5vj60.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-61j07.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-69b1h.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-6gns.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-6hadt.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-6kcqu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-6r76i.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-6s7tw.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-76ppv.md)
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-7jw10.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-7k8rb.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-7nwho.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-85ash.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-85x3i.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-87yvj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-89r8e.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-8jcaw.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-8lr5t.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-8lw11.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-8sst.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-8x5s1.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-9b3lk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-9x2qd.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-dboi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,indexingkey,getter%29-v7ux.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-117h4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-14z0w.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-189d8.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-1azo2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-1crrl.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-1h1h2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-1ivma.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-1nysv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-1qzrr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-23wo7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-2a05k.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-2smdh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-2uf8c.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-378nv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-3tnqy.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-3ycg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-46269.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-4jnoj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-4m254.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-4oh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-4p9q1.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-51yri.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-583yi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-5fsj5.md)
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-5s1hj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-5zao5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-6llym.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-6z56x.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-7r73j.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-7shxg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-8c998.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-8kudn.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-8wluq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-903lh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-9g93q.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-9u1uo.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-azfr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-f3s1.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-fcbf.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-lehi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-wdj7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-y7eq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-ycdv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource)](./entityproperty/init%28identifier,title%29-zx9d.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-13xnz.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-1bnq3.md)
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-1c5ws.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-1l8sl.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-1yowe.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-257r8.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-2bj5r.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-2rj9v.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-2w3e8.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-2w70y.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-39qz2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-3mw8u.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-3tff.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-48ueo.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-4dni8.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-4loqc.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-4n2ip.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-4pbwv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-4uijs.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-57f1s.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-5lgys.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-5sni8.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-5ulha.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-666jz.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-6acp.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-6dqqg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-6drke.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-6lz1t.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-6xtf5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-6zs71.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-76pb2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-79zya.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-7wd5t.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-83se5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-8c6rk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-8j12u.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-8rgn4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-8rhb1.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-8zjbm.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-9bfki.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-9j32a.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-i6t3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-ljxw.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,asyncgetter%29-q0zr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-18iqn.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-1aujk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-1bz54.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-1cqi9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-1i9vi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-1io91.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-1l849.md)
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-1mutr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-1rxvx.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-1s1of.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-1vw32.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-1z8bx.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-27zxe.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-2ebtz.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-2hkfs.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-2ivai.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-2o5qo.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-2s97i.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-2zad4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-2zctu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-390xu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-3ft8h.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-3gop3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-3x2sx.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-44mvn.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-46ynr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-4fibl.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-4imv0.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-4muq4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-4p2vn.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-5acor.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-5ae9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-5qxv6.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-5uvg5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-5zne0.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-64kpo.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-79kut.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-89tlg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-8pfo8.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-98md.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-9aj8g.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-9o3g5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-anop.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28identifier,title,customindexingkey%29-yryr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-15jom.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-17pv1.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-1bemi.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-1degd.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-1g1uu.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-1t0se.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-23cu.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-2g90j.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-2nemk.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-2sc73.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-3cqdb.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-3fq25.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-3swkh.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-4lew.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-4q6nr.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-4tlcf.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-5cnph.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-5dbm3.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-5jk65.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-5zbmo.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-6bnzj.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-6fzdg.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-6key7.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-6nhz5.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-6sbmw.md)
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-75c.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-7jt3a.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-88jun.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-8a3vv.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-8f8en.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-8kyt9.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-8pn52.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-8xa8o.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-8y886.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-90w4d.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-9bs0d.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-9damg.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-9f8kx.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-9k5or.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-9lbay.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-9ojmy.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-jxlb.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-ml3u.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,customindexingkey,asyncgetter%29-ygls.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-1lk96.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-25pox.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-2i6se.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-2w04l.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-33e4b.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-3tv4a.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-3wbqq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-4bw4h.md)
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-4ewbn.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-4hao9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-4ohyi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-4wabd.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-4wekz.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-55ec3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-58xo2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-5mo7k.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-5o1ml.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-60qr2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-62iyd.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-6dk4h.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-6pk7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-6z3sm.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-70r52.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-79rax.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-7kvdx.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-7o4mm.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-80ten.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-83cy4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-83rih.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-8b6zc.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-8bowp.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-8jx7j.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-8k5o7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-8mnme.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-8ns5q.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-8uv4q.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-8zcxx.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-99w0o.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-9eils.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-9gmb6.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-9mouf.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-9p6tz.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-h5gl.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getsetter%29-soy5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-16zlz.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-1e9p0.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-1ee1p.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-1gsrw.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-1mkk4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-1u0pg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-25een.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-295ww.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-2zrbu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-3uxvx.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-414a3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-4cps5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-4er40.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-4u40z.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-5211a.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-5aac4.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-5dmv4.md)
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-5j217.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-5nki5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-5swwl.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-6eti7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-6m6mv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-7jnk5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-7ns8d.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-7pbfj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-81l94.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-87vyt.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-8culv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-8ilsx.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-8ny42.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-8vt4c.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-9ati.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-9au2d.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-9mt17.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-9pk6n.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-9txqu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-9wx7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-9yntd.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-9ysll.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-ajvc.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-ij0w.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-mdrk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-ot1u.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,customindexingkey,getter%29-sykg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-13vpt.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-1bjxb.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-1m3gq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-202nc.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-22ywl.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-2ki7h.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-2qnfi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-2wlel.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-30j9o.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-314t.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-316ef.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-34xjy.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-34z2l.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-3f0hh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-3fdqs.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-3n23x.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-3nt3a.md)
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-3podv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-40xsb.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-4oqqg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-4xx1.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-543m.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-5cbob.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-5j2w0.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-62bbz.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-675df.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-6gjse.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-6iqrp.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-6qxo7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-7858.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-78e90.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-7bcmj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-7ih2c.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-7xyp7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-7y4ga.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-7yw8f.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-87x13.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-8tll6.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-9p3og.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-9pvof.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-9sctk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-h98w.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-lt86.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getsetter%29-xm9h.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-148sz.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-1kvdt.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-1p05z.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-20a0p.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-2jzos.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-2lyqk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-2siy3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-3dhy5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-3hwyu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-3ncc7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-3slre.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-402fk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-41eea.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-46hxc.md)
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-48n4e.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-4u6n9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-50b0e.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-5avq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-5hgyu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-5n6ev.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-5rda2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-5vb5n.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-606d7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-62h7m.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-638yo.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-69dif.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-6aexd.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-6cudy.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-6doj5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-6ed5h.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-6prgd.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-7dpwl.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-7r5sy.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-7v9k0.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-7y6pr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-7yl7s.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-7yz3u.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-8lcse.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-95t49.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-97xts.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-9hvo5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-9mfy6.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-rgp.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,getter%29-xk38.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-126me.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-13yp.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-140qh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-17sbg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-1d7eh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-1id3m.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-1oc13.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-1p0ni.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-24ubk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-2g7so.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-2igvi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-2lc65.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-2rsrn.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-2u5gr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-3e46e.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-3iz22.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-3lvfn.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-3w174.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-48ckw.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-4de5a.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-4f1tv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-4qn5e.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-4sj5q.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-4t4eo.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-5evk3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-5gnjk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-5lf3m.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-5ots1.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-5y81o.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-63pff.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-6njuf.md)
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-6z0g1.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-719ie.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-76y8o.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-771uy.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-8fqu6.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-8nym6.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-944mi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-9h6l7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-9j1ut.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-9qtrh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-9vp33.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-cajb.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28identifier,title,indexingkey%29-dkkw.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-1ewz9.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-1f85u.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-1pxpy.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-1tgg0.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-1wja4.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-206tv.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-2bdqz.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-2hi3p.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-2ieun.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-2ogte.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-3j0az.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-3pp6d.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-3y4e7.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-47j6b.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-48cy3.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-4gkwe.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-4hmy7.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-4imgx.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-4m37m.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-5oxik.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-5x9lq.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-654kf.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-6dzc3.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-6jp2s.md)
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-6qoau.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-6zl0n.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-7964x.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-7978r.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-7dhtc.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-7fdk7.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-7ufpz.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-7win5.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-7yrgp.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-83fyi.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-87y0x.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-8i7ay.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-8vc5j.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-9h942.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-9jfe5.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-9uer1.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-cf1m.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-g4dy.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-jg4p.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, asyncGetter: (Entity) async throws -> Value)](./entityproperty/init%28identifier,title,indexingkey,asyncgetter%29-ud7z.md)
  Creates an app intent entity property.  Do not call this directly, use @Property
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-105y3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-1hphk.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-1hvaq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-1l5wl.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-1q3zy.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-1ww98.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-2g83r.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-2hh8u.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-2iwfu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-2v29o.md)
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-2w265.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-3728b.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-3csno.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-3e7gq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-3pjwg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-3whod.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-41gci.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-41khy.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-42mzr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-46iih.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-4fq4c.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-4xy6b.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-4zpwo.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-599lq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-5imtx.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-5ntbj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-5tvf0.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-5vvd7.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-6ixm.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-72yrv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-7ngbf.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-7ukkh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-8p6zg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-8zs4n.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-9f972.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-9m8x3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-9myyf.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-9peuj.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-bkz9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-eep9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-j4b3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-kjwe.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-ljc8.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getSetter: WritableKeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getsetter%29-tmzu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-1ah3y.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-1b8aq.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-1hav2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-1ppna.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-28ia3.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-2afe.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-2ayhf.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-2fxl8.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-2jt5o.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-2u6ja.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-2vq8b.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-3pnfo.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-4holm.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-4lfwn.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-4m3tr.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-55ksi.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-58az0.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-5hncv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-5l3d9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-5ly72.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-5u97v.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-5zemv.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-61mk9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-6f0g9.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-6furm.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-6rif2.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-6syih.md)
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-6vvka.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-6wzai.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-7ky3z.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-7o17a.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-7qicg.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-86bq5.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-89tzd.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-8gtle.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-8ve8n.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-94hnb.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-993zw.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-9hszh.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-9msjb.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-9txwb.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-q29p.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-rwuu.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init<Entity>(identifier: String, title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>, getter: KeyPath<Entity, Value>)](./entityproperty/init%28identifier,title,indexingkey,getter%29-zvtb.md)
  Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-16blv.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-1c485.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-1jm7i.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-1tf6w.md)
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-24gfj.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-2s0xw.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-2tvny.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-36eo3.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-3hcko.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-3i9um.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-4erjr.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-4q74p.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-4swp4.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-4uaab.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-4un4q.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-4vo0w.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-50dym.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-54q22.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-5oigm.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-5r3ta.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-5uukx.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-62p8a.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-64hzn.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-67920.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-6ajfc.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-6s7ww.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-6ve4u.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-7ay2p.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-7fpdv.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-7pxdu.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-86ory.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-8bniy.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-8cjiy.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-8igu7.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-8khyg.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-8kiad.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-8ow58.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-8oyce.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-8s4qd.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-8s4w0.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-8y2li.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-9lt9d.md)
  Creates an app intent entity property.
- [convenience init<Entity>(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-9nke3.md)
  Creates an app intent entity property.
- [convenience init(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28indexingkey%29-9thiy.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-1d25v.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-1tc1v.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-28g4s.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-2dp76.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-2gm7f.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-2kb1u.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-2np59.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-2yle4.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-3887n.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-3d77p.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-3g21e.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-3h662.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-3nzru.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-3revp.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-3rjdp.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-4kz7s.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-4url0.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-4v3x3.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-4ziq1.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-58kn8.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-5pb1r.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-5sctd.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-5wa3x.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-6av70.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-6l4hm.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-6n85w.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-6tv32.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-6zgt6.md)
  Creates an app intent entity property.
- [convenience init<Entity>(title: LocalizedStringResource)](./entityproperty/init%28title%29-71itc.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-7a469.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-7dt1k.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-7e0g5.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-7txcv.md)
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-7z2pv.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-88r0j.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-8ayaj.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-8ykha.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-98ebz.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-9tfqf.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-9xd4p.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-djmw.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-f3c7.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-l1c6.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource)](./entityproperty/init%28title%29-r1fa.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-19tpd.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-1cly1.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-1kll9.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-1lk5r.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-1pon2.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-27f1h.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-29351.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-299oe.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-2eglc.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-2kgu7.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-2me54.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-2wpks.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-34nxo.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-36akc.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-36gcg.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-3k7y6.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-3y42t.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-40biq.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-43tsx.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-4b9on.md)
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-4ivjp.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-4jvux.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-4ppfn.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-4vub3.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-51xvr.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-5ot57.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-5p4up.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-5r7ga.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-5sp6u.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-5txeg.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-5u4ei.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-63fux.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-644dr.md)
  Creates an app intent entity property.
- [convenience init<Entity>(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-646pr.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-72srp.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-73f5l.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-7wvtv.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-8jbsy.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-8rlb5.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-987gm.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-98gxd.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-9jhf1.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-9k3g8.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./entityproperty/init%28title,customindexingkey%29-l7mf.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-15les.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-1ehae.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-1otqt.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-1v6ta.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-1vtfr.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-28z6k.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-2d05x.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-2t5xq.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-2zpkf.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-341lk.md)
  Creates an app intent entity property.
- [convenience init<Entity>(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-3bmky.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-3f9sk.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-3hivp.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-3jtzk.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-3kx80.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-3o7nw.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-3p35f.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-467g1.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-4ago.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-4dr01.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-4ke5t.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-4v678.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-5e492.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-5fi7j.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-5xk73.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-6dbum.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-6f87j.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-6fcb5.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-6qpbc.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-6woh7.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-7fomp.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-7j59q.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-7jpkk.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-7oyrf.md)
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-7silh.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-7vrqm.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-8nkkg.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-99msx.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-9bcw4.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-9dwm4.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-9j7hv.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-9txtw.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-9yblh.md)
  Creates an app intent entity property.
- [convenience init(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./entityproperty/init%28title,indexingkey%29-vhxo.md)
  Creates an app intent entity property.
### Instance Properties
- [var projectedValue: EntityProperty<Value>](./entityproperty/projectedvalue.md)
- [var wrappedValue: Value](./entityproperty/wrappedvalue.md)

## Relationships

### Conforms To
- [AnyIntentValue](./anyintentvalue.md)
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Property declarations
- [macro ComputedProperty()](./computedproperty%28%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource)](./computedproperty%28title%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./computedproperty%28indexingkey%29.md)
  A macro that adds a computed app entity property with get and set accessors.
- [macro ComputedProperty(customIndexingKey: CSCustomAttributeKey)](./computedproperty%28customindexingkey%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./computedproperty%28title,customindexingkey%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./computedproperty%28title,indexingkey%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro DeferredProperty()](./deferredproperty%28%29.md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [macro DeferredProperty(title: LocalizedStringResource)](./deferredproperty%28title%29.md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [macro DeferredProperty(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./deferredproperty%28indexingkey%29.md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [macro DeferredProperty(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./deferredproperty%28title,indexingkey%29.md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [struct EntityPropertyModifiers](./entitypropertymodifiers.md)
- [Property comparators](./property-comparators.md)
  Specify the type of comparison to perform during a property-matched query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty)*