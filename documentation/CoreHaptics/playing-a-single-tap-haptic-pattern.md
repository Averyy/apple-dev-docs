# Playing a single-tap haptic pattern

**Framework**: Core Haptics

Create and play a transient haptic pattern from a dictionary literal inline.

#### Overview

This article describes how to define the haptic pattern for a single haptic tap and how to play that haptic pattern through a haptic engine.

##### Create a Haptic Engine

The [`CHHapticEngine`](chhapticengine.md) is your app’s interface to the haptic device. An instance of a haptic engine allows you to create a [`CHHapticPatternPlayer`](chhapticpatternplayer.md) or [`CHHapticAdvancedPatternPlayer`](chhapticadvancedpatternplayer.md) to play individual haptics. Create the haptic engine as described in [`Preparing your app to play haptics`](preparing-your-app-to-play-haptics.md).

##### Specify a Dictionary Literal

The next step is to create a dictionary literal representing the haptic. The following represents a single haptic tap:

**Swift**:

```swift
let hapticDict = [
    CHHapticPattern.Key.pattern: [
        [CHHapticPattern.Key.event: [
            CHHapticPattern.Key.eventType: CHHapticEvent.EventType.hapticTransient,
            CHHapticPattern.Key.time: CHHapticTimeImmediate,
            CHHapticPattern.Key.eventDuration: 1.0]
        ]
    ]
]
```

**Objective-C**:

```objc
NSDictionary* hapticDict = @{
    CHHapticPatternKeyPattern: @[ 
        @{ CHHapticPatternKeyEvent: @{
            CHHapticPatternKeyEventType: CHHapticEventTypeHapticTransient,
            CHHapticPatternKeyTime: @(CHHapticTimeImmediate),
            CHHapticPatternKeyEventDuration: @1.0 },
        },
    ],
};
```

Each entry in the dictionary shown above is a haptic event, with an event type, a start time, and a duration. In this case, the event type is [`hapticTransient`](chhapticevent/eventtype/haptictransient.md) because a single tap is a transient pattern — a quick impulse. The time is `CHHapticTimeImmediate` to indicate that the event begins immediately, right after time `0`. The duration of `1.0` indicates that the event lasts one second.

##### Create a Haptic Pattern Player From the Dictionary

Initialize a [`CHHapticPattern`](chhapticpattern.md) from the dictionary you just created.

**Swift**:

```swift
let pattern = try CHHapticPattern(dictionary: hapticDict)
```

**Objective-C**:

```objc
NSError* error;
CHHapticPattern* pattern = [[CHHapticPattern alloc] initWithDictionary:hapticDict error:&error];
```

When you’re ready to play your haptic, create a player for that pattern. Each player is responsible for playing one pattern. You can reuse a player to play its pattern as many times as you like.

Use one of the haptic engine’s factory methods, like [`makePlayer(with:)`](chhapticengine/makeplayer(with:).md), to create the haptic pattern player.

**Swift**:

```swift
let player = try engine.makePlayer(with: pattern)
```

**Objective-C**:

```objc
NSError* error = nil;
id<CHHapticPatternPlayer> player = [_engine createPlayerWithPattern:pattern error:&error];
```

If you call [`start(atTime:)`](chhapticpatternplayer/start(attime:).md) on a player that’s already playing, it restarts itself at the beginning of the pattern.

Haptic players are inexpensive, lightweight objects, so create and discard them freely. Unless your app requires real-time, latency-free haptic feedback in response to user interaction — like precise ticks on a dial — you can create your player right before playing the haptic.

##### Start the Engine and Play the Haptic Pattern

Start the haptic engine before you play a haptic player, and stop the engine once you’ve finished playing all haptic patterns. Play the haptic by calling the player’s [`start(atTime:)`](chhapticpatternplayer/start(attime:).md) method.

**Swift**:

```swift
// Stop the engine after it completes the playback.
engine.notifyWhenPlayersFinished { error in
    return .stopEngine
}

try engine.start()
try player.start(atTime: 0)
```

**Objective-C**:

```objc
// Stop the engine after it completes the playback.
[_engine notifyWhenPlayersFinished:^CHHapticEngineFinishedAction(NSError * _Nullable error) {
    return CHHapticEngineFinishedActionStopEngine;
}];
    
[_engine startWithCompletionHandler:^(NSError* returnedError) {
    NSError* error;
    [self.player startAtTime:0 error:&error];
}];
```

If the engine is in a running state when you call [`start()`](chhapticengine/start().md), the system plays the haptic at the scheduled time. Playback follows a “fire and forget” model, so your app doesn’t need to keep the player and pattern in memory once you’ve called [`start()`](chhapticengine/start().md). You need to retain your engine so it doesn’t exit scope during your program.

Unless you’re playing several haptic patterns in succession, bookend haptic playback with starting and stopping the engine. Starting the engine ensures that the haptic engine is in a running state when you schedule a haptic to play. Stopping the engine after you finish playing the haptic conserves power and allows it to prepare for the next time your app needs haptic playback. Be aware that your engine may stop on its own in auto-shutdown mode.

## See Also

- [Preparing your app to play haptics](preparing-your-app-to-play-haptics.md)
  Set up your app to play haptics.
- [class CHHapticEngine](chhapticengine.md)
  An object that represents the connection to the haptic server.
- [class CHHapticPattern](chhapticpattern.md)
  An object representing a haptic waveform.
- [protocol CHHapticPatternPlayer](chhapticpatternplayer.md)
  A protocol that defines a standard pattern player capable of playing haptic patterns with fixed parameters.
- [protocol CHHapticAdvancedPatternPlayer](chhapticadvancedpatternplayer.md)
  A protocol that defines an advanced pattern player capable of looping, seeking, pausing, and resuming haptic playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/playing-a-single-tap-haptic-pattern)*